import requests

#GET
request = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# print(request)
print(request.status_code)
# print(request.text)
my_query = request.json()
print(my_query['title'])

#POST
post = requests.post('https://jsonplaceholder.typicode.com/posts', data={
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  })
print(post.status_code)
