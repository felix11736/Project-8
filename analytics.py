from confluent_kafka import Consumer
import sentiment_analysis as sa
import ast

################

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer', 'auto.offset.reset': 'latest'})

print('Available topics to consume: ', c.list_topics().topics)

c.subscribe(['sentences'])

################

def main():
    while True:
        msg = c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data = msg.value().decode('utf-8')

        data = ast.literal_eval(data)

        output = sa.SentimentAnalysis(data['sentence']).execute()

        print(output)

    c.close()

if __name__ == '__main__':
    main()