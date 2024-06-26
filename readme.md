# Configuration

1. To run repo u have to habe open_ai api key defined in your env variables as "APIKEY-OPENAI" key.
2. You can configure which task should be perform, there is .env file which contains configuration. It has two keys: TASK - this key define which task will be handle during processing, CLIENT - some of task have two solution one for directly OpenAI API, and the second with using LangChain + OpenAI API, by defining this value u can choose which client should be used.

```
TASK=search
CLIENT=langchain
```

3. To run the program, just ran the main.py file

```python
python main.py
```

## Tasks details:

1. Search Task requires vectordatabase to process. I decided to use qdrant and sentence-transformers to embeded my information. To run qdrant you can build e.g. python script which will run the local instance for u (it has to be on 6333 port), or u can run docker instance with qdrant. In my solution I ran qdrant on docker (qdrant/qdrant:latest image)

Additional useful commands to manage docker (rembmer to run in linux shell):

- to run qdrant container on port 6333 if u dont have image it will download it automatically:
- second command do the same but I added --name property which allows us to name our image, seems quite useful

```shell
docker run -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage qdrant/qdrant

docker run -d -p 19530:19530 --name milvus milvusdb/milvus:2.4-latest-gpu
```

- to display all images with statuses, ids and names. This command allow u to identify status of your image.

```shell
docker ps -a
```

- to remove docker image, e.g. if u have already qdrant image and u want to remove it to make space for another with the same name u can use this command

```shell
docker rm -f milvus_in_memory
```

- to display logs for the pointed name (I think it will also work for id). It helps to investiage why e.g. buling your image has failed

```shell
docker logs milvus
```

2. People task requires to refactor token is valid only 2 minutes and creation of VDB takes too long - currently u have to create DB and then run script again with commented lines which genrates embeddings. Embedding generation takes like 5 minutes so it has to be done before running task. It requires to refactor, generating db should be run in config scirpt or sth like that.

3. ownapi and ownapipro task is in diffrent repo, it required to run own api server so I decided to move it to [separate repo](https://github.com/MichealRG/aidevs_flask_app) to run flask server

4. meme: renderfrom it requries to set key as env var, here is link to template: https://renderform.io/console/template/html-editor/?templateId=round-devils-return-clearly-1122 to use with body:

```json
{
  "template": "round-devils-return-clearly-1122",
  "data": {
    "title": "Gdy koledzy z pracy mówią, że ta cała automatyzacja to tylko chwilowa moda, a Ty właśnie zastąpiłeś ich jednym, prostym skryptem",
    "image-url": "https://tasks.aidevs.pl/data/monkey.png"
  }
}
```

5. optimaldb - [RESULT OF TASK]: Response msg: {'code': 0, 'msg': 'OK', 'note': 'CORRECT', 'questions': '\n1. Jaka jest ulubiona gra Zygfryda?\n2. W jakim sklepie pracuje Stefan?\n3. Jaki jest ulubiony film Zygfryda?\n4. Jaki taniec weselny wybrał Zygfryd na swoim weselu?\n5. Co studiuje Ania?\n6. Jak nazywa się\xa0inspiracja fitness Ani? \n', 'answers': '1. Ulubiona gra Zygfryda to "Terra Mystica".\n2. Stefan pracuje w sklepie Żabka.\n3. Ulubiony film Zygfryda to "Matrix".\n4. Zygfryd wybrał tango jako taniec weselny.\n5. Ania studiuje prawo.\n6. Inspiracją fitness Ani jest Jennifer Lopez (J.Lo).'}
