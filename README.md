# kong-api-rate-limiting
🚀 API Rate Limiting with Kong API Gateway

This repository demonstrates how to implement API Rate Limiting using Kong API Gateway with Redis-based distributed limits. The setup includes:

✅ Kong API Gateway (for traffic management)

✅ Redis (for distributed rate limiting)

✅ PostgreSQL (for Kong database storage)

✅ Docker Compose (for easy deployment)

## 📌 Features

✔ Rate Limiting per IP, API Key, or Consumer

✔ Redis-based distributed Rate Limiting for scalability

✔ Multiple Rate Limits (Per Second, Minute, Hour)

✔ Monitoring via Kong Admin API

## 📌 Prerequisites

🔹 Docker & Docker Compose installed → Get Docker

🔹 Curl or Postman for API testing

🚀 Step 1: Clone the Repository

```bash
git clone https://github.com/kelwin-d/kong-api-rate-limiting.git
cd kong-api-rate-limiting
```

🚀 Step 2: Start Kong, Redis & PostgreSQL Using Docker

```bash
docker-compose up -d
```
✅ This starts Kong API Gateway, Redis, and PostgreSQL.

🚀 Step 3: Configure Kong API Rate Limiting Plugin

## 1️⃣ Enable Rate Limiting on an API Service

```bash
curl -X POST http://localhost:8001/services/my-api/plugins \
  --data "name=rate-limiting" \
  --data "config.minute=100" \
  --data "config.policy=redis" \
  --data "config.redis_host=redis"
```
✔ Limits API calls to 100 per minute using Redis.

## 2️⃣ Apply Rate Limiting Per Consumer (API Key-based Limit)

```bash
curl -X POST http://localhost:8001/consumers/my-consumer/plugins \
  --data "name=rate-limiting" \
  --data "config.minute=50" \
  --data "config.policy=redis" \
  --data "config.redis_host=redis"
```
✔ Limits API requests to 50 per minute per consumer.

## 3️⃣ Apply Rate Limiting Per Route

```bash
curl -X POST http://localhost:8001/routes/my-route/plugins \
  --data "name=rate-limiting" \
  --data "config.hour=500" \
  --data "config.policy=cluster"
```
✔ Limits 500 API requests per hour for a specific route.

🚀 Step 4: Test API Rate Limiting

Run this command to send 20 API requests quickly:

```bash
for i in {1..20}; do curl -i http://localhost:8000/my-api; done
```

🔹 Expected Behavior:

First 10 requests succeed.
After 10 requests, Kong blocks further requests and returns:

```bash
{
  "message": "API rate limit exceeded. Try again later."
}
```

🚀 Step 5: Monitor API Rate Limits

Check Active Rate Limits

```bash
curl -X GET http://localhost:8001/plugins?name=rate-limiting
```

Check Kong Logs

```bash
docker logs -f kong
```

## 📌 Troubleshooting

🔹 If Kong does not start, check Docker logs:

```bash
docker logs -f kong
```

🔹 If API requests exceed limits unexpectedly, verify Redis is running:

```bash
docker ps | grep redis
```

## 📌 Contributing
Feel free to fork this repo, open issues, and submit pull requests!

## 📌 License
This project is open-source and available under the MIT License.
