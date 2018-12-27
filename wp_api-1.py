import requests,unittest,pprint

class WpApi_Test(unittest.TestCase):

      def setUp(self):
          self.wp_url="http://192.168.74.128:80/wordpress/index.php/wp-json/wp/v2/"
          self.headers={'Authorization':'Basic dGVzdDE6TDA3WSBRSGZNIGJGT0YgYWxWdiA5dW9IIGEyYmQ='}

      def get(self,endpoint,params):
          real_endpoint=self.wp_url+endpoint
          return requests.request("GET",real_endpoint,headers=self.headers,params=params)

      def post(self,endpoint,params):
          real_endpoint=self.wp_url+endpoint
          return requests.request("POST",real_endpoint,headers=self.headers,params=params)

      def get_json(self,endpoint,params):
          return self.get(endpoint,params).json()

      print("******************test case********************")

      # 根据id获取一篇文章
      def test_get_post_by_id(self):
          data = {"id":1}
          '''
          res = self.get("posts", data)
          print(res.status_code)
          pprint.pprint(res.json())
          print(res.json())
          '''
          res = self.get_json("posts", data)
          #pprint.pprint(res)

      # 删除一篇文章
      def test_delete_post_by_id(self):
          #data={"id":5}
          res=requests.request("DELETE",self.wp_url+"posts/5",headers=self.headers).json()
          pprint.pprint(res)
          #self.assertEqual(res['id'],5)



'''
      #3A
      #分页显示listpost
      def test_get_only_one_post_using_post_list_api(self):
          querystring={"per_page":1}#分页
          res=self.get_json("posts",querystring)
          #pprint.pprint(res)
          #print(res)

          self.assertEqual(len(res),querystring['per_page'])
          self.assertEqual(res[0]['status'],'publish')

      print("***********************************")

      #发布文章
      def test_creat_post(self):
          postData={"title":"new title","content":"new contetn"}
          res=self.post("posts",postData)
          print(res)
          print(res.json())
          self.assertEqual(res.json()['code'],'OK')
          print(res.status_code)
          self.assertEqual(res.status_code,200)
          print(res.url)
          #print(res.headers)
'''



      #修改一篇文章



if __name__=='__main__':
      unittest.main()