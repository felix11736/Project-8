from wonderwords import RandomSentence
from confluent_kafka import Producer
import json
import time
import logging
import sys
import random

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

p = Producer({'bootstrap.servers':'localhost:9092'})

#####################

def receipt(err, msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

#####################
print('Kafka Producer has been initiated...')

s = RandomSentence()

def main():
    while True:
        # a sentence with a subject, predicate, adjective and direct object
        data = {
            'sentence': s.sentence()
        }

        m = json.dumps(data)
        p.poll(1)
        p.produce('sentences', m.encode('utf-8'), callback=receipt)
        p.flush()

if __name__ == '__main__':
    main()