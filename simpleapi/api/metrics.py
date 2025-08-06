from prometheus_client import Counter


REQUEST_COUNTER = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status_code']
)

# Основные метрики
# 1. Counter (счетчик)
# from django_prometheus import metrics

# # Создаем счетчик
# REQUESTS_COUNTER = metrics.Counter(
#     'myapp_requests_total', 
#     'Total number of requests',
#     ['endpoint', 'method']  # Метки (labels)
# )

# @api_view(['GET'])
# def hello_world(request):
#     # Инкрементируем счетчик с метками
#     REQUESTS_COUNTER.labels(
#         endpoint='/hello', 
#         method='GET'
#     ).inc()
    
#     return Response({"message": "Hello, World!"})

# 2. Gauge (измеритель)
# ACTIVE_USERS_GAUGE = metrics.Gauge(
#     'myapp_active_users',
#     'Number of active users'
# )

# def login_view(request):
#     ACTIVE_USERS_GAUGE.inc()  # Увеличиваем при логине
#     # ... логика входа

# def logout_view(request):
#     ACTIVE_USERS_GAUGE.dec()  # Уменьшаем при логауте
#     # ... логика выхода

# 3. Histogram (гистограмма)
# from django_prometheus import metrics
# import time

# REQUEST_TIME_HISTOGRAM = metrics.Histogram(
#     'myapp_request_latency_seconds',
#     'Request processing time histogram',
#     ['endpoint'],
#     buckets=(0.1, 0.5, 1.0, 2.5, 5.0, 10.0)  # Границы корзин
# )

# @api_view(['GET'])
# def hello_world(request):
#     start_time = time.time()
    
#     try:
#         response = Response({"message": "Hello, World!"})
#         return response
#     finally:
#         # Фиксируем время выполнения
#         REQUEST_TIME_HISTOGRAM.labels(
#             endpoint='/hello'
#         ).observe(time.time() - start_time)


# 4. Summary (сводка)
# RESPONSE_SIZE_SUMMARY = metrics.Summary(
#     'myapp_response_size_bytes',
#     'Size of HTTP responses',
#     ['endpoint']
# )

# @api_view(['GET'])
# def hello_world(request):
#     response = Response({"message": "Hello, World!"})
    
#     # Фиксируем размер ответа
#     RESPONSE_SIZE_SUMMARY.labels(
#         endpoint='/hello'
#     ).observe(len(response.content))
    
#     return response