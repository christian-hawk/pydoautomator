from pydantic import BaseModel
from typing import List, Optional


class Droplet(BaseModel):
    id: Optional[int] = None
    name: str
    region: str = 'nyc1'
    size: str = 's-8vcpu-16gb'
    image: int
    ssh_keys: List[int] = []
    private_networking: bool = True
    vpc_uuid: str = None
    monitoring: bool = True
    tags: List[str] = []
