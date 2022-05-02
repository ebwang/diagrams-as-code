from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ALB
from diagrams.aws.network import Route53

with Diagram("Clustered Web Services", show=False):
    dns = Route53("dns")
    lb = ALB("alb")

    with Cluster("Services"):
        svc_group = [EC2("web1"),
                     EC2("web2"),
                     EC2("web3")]

    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    redis = ElastiCache("Redis")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> redis