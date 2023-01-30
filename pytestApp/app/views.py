
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializer import ClientSerializer,ProjectsSerializer,ProjectUserSerializer

from .models import Client,Projects,Project_Users
import datetime


#logged in used id
_SESSION={'USER_ID':2}

@api_view(['GET','POST'])
def fetch_clients(request):
    if(_SESSION['USER_ID'] is None):

        return Response(status=400,data={'message':'invalid user'})

    if request.method=='GET':
        data=Client.objects.all()
        
        serialzer=ClientSerializer(data,many=True)
        return Response(serialzer.data)
    
    elif request.method=='POST':
        try:
            info=request.data
            info['created_by']=_SESSION['USER_ID']
            print(info)
            serialzer=ClientSerializer(data=info)
            if serialzer.is_valid():
                try:
                    serialzer.save()
                    return Response(serialzer.data)
                except Exception as e:
                    print(e)
                    return Response(status = 400,data={'message':'something went wrong!'})
                
            
            return Response(status = 400,data={'message':'invalid data'})
        
    
        except Exception as e:
            print(e)
            return Response(status = 400,data={'message':'invalid data'})
        
    

        

@api_view(['GET','PATCH','DELETE'])
def client_details(request,id):
    if(_SESSION['USER_ID'] is None):

        return Response(status=400,data={'message':'invalid user'})
    
    if(request.method=='GET'):
    
        try:
            data=Client.objects.get(id=id)
            serialzer=ClientSerializer(data)
            res=dict(serialzer.data)
            res['projects']={}
            
            try:
                pro_data=Projects.objects.filter(client_id=id).all()
                pro_data=ProjectsSerializer(pro_data,many=True).data
                res['projects']=[{'id':p['id'],'project_name':p['project_name']} for p in pro_data]
                # res['projects']=pro_data
            except Exception as e1:
                print(e1)
                
        

            return Response(res)
        
        except Exception as e:

            print(e)

            return Response(status=400,data={'message':'invalid request'})
        
    elif request.method=='PATCH':
        try:
            data=request.data
            obj=Client.objects.get(id=id)
            # obj['updated_at']=datetime.datetime.now()
                
            serialzer=ClientSerializer(obj,data=data,partial=True)
            if serialzer.is_valid():
                serialzer.save()
                return Response(serialzer.data)
            
            return Response(status=400,data={'message':'invalid details'})
    
        except Exception as e:
            print(e)

            return Response(status=400,data={'message':'invalid request'})
        
    elif request.method=='DELETE':
        try:
            data=request.data
            obj=Client.objects.get(id=id)
            obj.delete()
            
            return Response(status=204)
    
        except Exception as e:
            print(e)

            return Response(status=400,data={'message':'invalid id'})

    

@api_view(['Post'])
def create_project(request,id):

    if(_SESSION['USER_ID'] is None):

        return Response(status=400,data={'message':'invalid user'})
    
    try:
        info=request.data
        info['client_id']=id
        info['created_by']=_SESSION['USER_ID']

        p_users=[e for e in  info['users']]

        del info['users']
        


        print(info)
        serialzer=ProjectsSerializer(data=info)
        if serialzer.is_valid():
            try:
                obj=serialzer.save()
                print('pid',obj.id)

                for u in p_users:
                    up={'project_id':obj.id,'User_id':u['id']}
                    ups=ProjectUserSerializer(data=up)
                    ups.is_valid()
                    ups.save()


                return Response(serialzer.data)
            except Exception as e:
                print(e)
                return Response(status = 400,data={'message':'something went wrong!'})
            
        
        return Response(status = 400,data={'message':'invalid data'})
    

    except Exception as e:
        print(e)
        return Response(status = 400,data={'message':'invalid data'})
    

@api_view(['GET'])
def fetch_projects(request):

    if(_SESSION['USER_ID'] is None):

        return Response(status=400,data={'message':'invalid user'})
       
    try:
        user_id=str(_SESSION['USER_ID'])
        pro_data=Project_Users.objects.filter(User_id=user_id).all()
        print(pro_data)
        projects=ProjectUserSerializer(pro_data,many=True).data
        print(projects)
        return Response(projects)
    
    except Exception as e:

        print(e)

        return Response(status=400,data={'message':'invalid request'})