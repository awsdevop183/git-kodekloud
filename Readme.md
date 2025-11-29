```cd backend
docker build -t YOUR_DOCKERHUB_USERNAME/k8s-backend-sqlite:latest .
docker push YOUR_DOCKERHUB_USERNAME/k8s-backend-sqlite:latest


```

kubectl apply -f manifests/backend.yaml

kubectl get pods -l app=demo-backend
kubectl get svc backend-service
