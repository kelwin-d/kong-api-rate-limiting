import redis
from flask import Flask, request, jsonify

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

RATE_LIMIT = 5  # 5 requests per minute
TIME_WINDOW = 60  # 60 seconds

@app.route('/api/resource', methods=['GET'])
def rate_limited_resource():
    user_ip = request.remote_addr
    key = f"rate_limit:{user_ip}"

    current_count = redis_client.get(key)
    
    if current_count and int(current_count) >= RATE_LIMIT:
        return jsonify({"error": "Rate limit exceeded. Try again later."}), 429

    redis_client.incr(key)
    redis_client.expire(key, TIME_WINDOW)

    return jsonify({"message": "Request successful!"})

if __name__ == '__main__':
    app.run(debug=True)

