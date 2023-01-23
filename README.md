# System to register request from people

### Stack : tornado(as front and back end for creating requests) - rabbbitMQ - fastapi_consumer - postgresql 

## Project structure


-- _backend_ ( tornado with _few_ html page with __form__ for input information and move to rabbitmq)

-- _rabbitmq_

-- _fastapi_consumer_ (api for listening messages from rabbitMQ queue and save data to postgresql)

-- _docker-compose.yml_ (file for deploying with containers)

-- _venv_ (not useful , only for developing stage )


# Instruction to launch on containers with Docker
__Unfortunately__ I couldn't adjust containers to startup with strict order 

I tried docker compose parameters:__depends_on__ and __link__ , __network_mode__ and etc. , but nothing didn't help .

And for my realization it became a trouble and I solved it with manually startuping each container by this ___order___ 

__(don't do step up before container isn't ready)__ : 

1. db (postgresql)
2. adminer (localhost:8080) - for monitoring changes in db __for connecting check env variables for db__
3. my-rabbitmq
4. backend (tornado)
5. fastapi 
---



And wait  ✨Magic ✨

---
### To test working: 
Go to http://localhost:81 (it doesn't want to work on 80 port and I changed it on 81)
Fill out the form with your values and click button "Отправить"
And you will can check the information in db , and some info in container's consoles in Dokcer Desktop app.

