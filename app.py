import json
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def download_file(output_file_path, download_url):
    # 判断文件是否已经存在
    if not os.path.exists(output_file_path):
        try:
            response = requests.get(download_url)
            if response.status_code == 200:
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                with open(output_file_path, 'wb') as output_file:
                    output_file.write(response.content)
                print(f"文件已下载并保存到: {output_file_path}")
            else:
                print(f"下载文件失败: {download_url}")
        except Exception as e:
            print(f"下载文件出现错误: {download_url} - 错误信息: {e}")
    else:
        print(f"文件已存在: {output_file_path}")
        
# 基础URL
base_url = 'firmware-selector.openwrt.org'

# 引导文件路径
guide_file_path = 'tmp.json'

with open(guide_file_path, 'r') as file:
    guide_data = json.load(file)

for release in list(guide_data.keys()):
    download_overview_url = f"https://{base_url}/data/{release}/overview.json"
    # overview文件路径
    overview_path = f'./www/data/{release}/overview.json'
    
    download_file(overview_path, download_overview_url)
    
    # overview文件
    with open(overview_path, 'r') as file:
        overview_data = json.load(file)

    # 解析引导文件内容
    profiles = overview_data.get('profiles', [])
    release = overview_data.get('release')

    def download_profile_id_file(profile):
        profile_id = profile.get('id')
        target = profile.get('target')
        
        # 生成下载URL
        download_url = f"https://{base_url}/data/{release}/{target}/{profile_id}.json"
        
        # 生成文件保存路径
        output_file_path = os.path.join(f"./www/data/{release}/{target}", f"{profile_id}.json")
        download_file(output_file_path, download_url)

    # 使用多线程并发下载
    batch_size = 300

    # 将profiles按batch_size分组
    profile_batches = [profiles[i:i + batch_size] for i in range(0, len(profiles), batch_size)]

    for batch in profile_batches:
        with ThreadPoolExecutor(max_workers=batch_size) as executor:
            future_to_profile = {executor.submit(download_profile_id_file, profile): profile for profile in batch}
            for future in as_completed(future_to_profile):
                profile = future_to_profile[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"处理profile {profile.get('id')} 时出现错误: {e}")
    print(f"版本{release}处理完毕")  
    
print("所有文件处理完毕")
