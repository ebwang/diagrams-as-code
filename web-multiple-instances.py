from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import ElastiCache
from diagrams.aws.network import ALB, DirectConnect
from diagrams.oci.compute import VM
from diagrams.aws.storage import EFS
from diagrams.elastic.observability import APM
from diagrams.saas.cdn import Akamai


with Diagram("Web Diagram", show=True):
    dns = Akamai("dns")
    lb = ALB("alb")

    with Cluster("EC2 Webs"):
        svc_webs = [ EC2("web1"),
                    EC2("web2"),
                     EC2("web3")]
        svc_web_primary = svc_webs[1]

    db_primary = VM("OCI db1")
    elk_apm = APM("ELK-APM")
    redis = ElastiCache("AWS Redis")
    efs = EFS("AWS EFS")
    direct_connect = DirectConnect("AWS-EQUINIX")

    dns >> lb 
    lb >> svc_web_primary >> direct_connect >> db_primary
    svc_web_primary >> redis
    svc_web_primary >> efs
    svc_web_primary >> elk_apm