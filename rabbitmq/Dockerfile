FROM rabbitmq

RUN rabbitmq-plugins enable --offline rabbitmq_management
RUN rabbitmq-plugins enable rabbitmq_shovel rabbitmq_shovel_management

EXPOSE 15671 15672