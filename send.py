import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


num = [10, 100, 56]

for i in num:
    channel.basic_publish(exchange='', routing_key='hello', body=str(i).encode('utf-8'))
    print(i)

connection.close()
