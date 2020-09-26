from pydantic import BaseModel
from typing import List, Optional


class Droplet(BaseModel):
    id: int
    name: str
    region: str = 'nyc1'
    size: str = 's-8vcpu-16gb'
    image: int
    ssh_keys: List[int] = []
    private_networking: bool = True
    vpc_uuid: int
    monitoring: bool = True
