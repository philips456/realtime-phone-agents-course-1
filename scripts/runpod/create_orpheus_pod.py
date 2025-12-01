import runpod
from realtime_phone_agents.config import settings

runpod.api_key = settings.runpod.api_key

pod_id = runpod.create_pod(
    name="Orpheus Server",
    image_name="theneuralmaze/orpheus-llamacpp-server:latest",
    gpu_type_id="NVIDIA GeForce RTX 5090",
    cloud_type="SECURE",
    gpu_count=1,
    volume_in_gb=20,
    volume_mount_path="/workspace",
    ports="8080/http",
)

print(f"Pod created: {pod_id}")