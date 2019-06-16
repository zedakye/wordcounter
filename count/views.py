from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def homepage(request):
	return render(request,'count/base.html')
def count(request):
	data = request.GET['fulltextarea']
	li=data.split()
	word=len(li)
	dic=dict()
	for i in li:
		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1
	sorted_list = sorted(dic.items(),key=operator.itemgetter(1))
	return render(request,'count/count.html',{'text':data,'words':word,'dic':sorted_list})
def about(request):
	return render(request,'count/about.html')