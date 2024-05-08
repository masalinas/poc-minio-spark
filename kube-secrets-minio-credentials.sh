kubectl create secret generic minio-secret \
--from-literal=AWS_ACCESS_KEY_ID=gl8rbGORHSpxmg1V \
--from-literal=AWS_SECRET_ACCESS_KEY=8WphDMckYqRb29s43SzA4trsV2GgaQRc \
--from-literal=ENDPOINT=gsdpi-hl.default.svc.cluster.local:9000 \
--from-literal=AWS_REGION=us-east-1 \
--namespace spark-operator
