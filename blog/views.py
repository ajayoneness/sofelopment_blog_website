from django.shortcuts import render,redirect
from django.http import HttpResponse
from info.models import blog_table,comments
from datetime import datetime
category=['technology','sports','Entertainments','Love','Lifestyle']
def index(request):
    lis=[]
    blg=blog_table.objects.all()
    #print(blg.count())
    for i in range (0, len(blg)):
        blog=[blg[i].id ,blg[i].title,blg[i].des,blg[i].youtube_link,blg[i].date,blg[i].time,blg[i].image,blg[i].subscribe,blg[i].category,blg[i].pub_draft]
        print("blog id : ",blg[i].pub_draft)
        fil= comments.objects.filter(post_id=blg[i].id)
        #print(fil)
        blog.append(fil)
        lis.append(blog)

    #comment
    if request.POST:
        postno = request.POST['postno']
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cmob = request.POST['cmob']
        comment = request.POST['cmt']
        timedate= datetime.now()
        print(timedate)
        commentpost = comments(name =cname,email=cemail,mob_no=cmob,comment=comment,post_id_id = int(postno),date_time=str(timedate))
        commentpost.save()

        post_no = [i.id for i in blg]
        return render(request, 'index.html', {'lis': lis, 'postno': post_no,'cat': category})

    post_no = [ i.id for i in blg]
    #print(lis)
    return render(request,'index.html',{'lis':lis,'postno':post_no,'cat': category,'aj':"All Posts"})


def adminlogin(request):
    if request.POST:
        uname = request.POST['uname']
        upsw = request.POST['psw']
        if uname == 'admin' and upsw == 'admin':
            return redirect('http://127.0.0.1:8000/showall/')

    return render(request,"login.html")

def createPost(request):
    if request.POST:
        cate = request.POST['category']
        title = request.POST['title']
        dec = request.POST['dec']
        youtube = request.POST['ytub']
        today = datetime.now()
        date = today.strftime("%Y-%m-%d")
        time = today.strftime("%H:%M:%S")
        image = request.POST['image']
        blogpost = blog_table(title=title,des=dec,category=cate,pub_draft=True,youtube_link=youtube,date=date,time=time,image=image)
        blogpost.save()
        return redirect('http://127.0.0.1:8000/')

    return render(request, "post.html",{'cat':category})



def draft(request):
    if request.POST:
        cate = request.POST['category']
        title = request.POST['title']
        dec = request.POST['dec']
        youtube = request.POST['ytub']
        date = request.POST['date']
        time = request.POST['time']
        image = request.POST['image']
        blogpost = blog_table(title=title,des=dec,category=cate,pub_draft=False,youtube_link=youtube,date=date,time=time,image=image)
        blogpost.save()
        return HttpResponse('Save in draft')
    else:
        return HttpResponse("codeAj")

def cat(request,aj):
    lis = []
    blg = blog_table.objects.filter(category=f"{aj}")
    # print(blg.count())
    for i in range(0, len(blg)):
        blog = [blg[i].id, blg[i].title, blg[i].des, blg[i].youtube_link, blg[i].date, blg[i].time, blg[i].image,
                blg[i].subscribe, blg[i].category, blg[i].pub_draft]
        print("blog id : ", blg[i].pub_draft)
        fil = comments.objects.filter(post_id=blg[i].id)
        # print(fil)
        blog.append(fil)
        lis.append(blog)

    post_no = [i.id for i in blg]
    # print(lis)
    return render(request, 'index.html', {'lis': lis, 'postno': post_no, 'cat': category,'aj':aj})


def showall(request):
    posts=blog_table.objects.all()

    return render (request,'showall.html',{'posts':posts})

def delete(request,obj):
    blog_table.objects.filter(id=obj).delete()

    posts = blog_table.objects.all()
    return render (request,'showall.html',{'posts':posts})

def edit(request,id):
    data=blog_table.objects.filter(id=id)

    return render (request,'post.html',{'data':data})
