from django.shortcuts import render
from .forms import UserRegisterForm, QuestionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.

def home(request):
    user= request.user
    print(user)
    return render(request, 'home.html', {"user":user})

def loginView(request):
    return render(request, 'login.html')

def Login(request):
    if request.method == 'POST':
        data= request.POST
        email = request.POST['email']
        password = request.POST['password1']
        userObj=User.objects.filter(email= email).values()
        #user= User.objects.filter(email=email)
        try:
            username=userObj[0]['username']
        except :
            username= None
        #print(user, username)
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return render(request,'home.html')
        else:
            data="Invalid Credentials"
            return render(request, 'login.html', {"data": data})

def signUpView(request):
    return render(request, 'signUp.html')

def signUp(request):
    if request.method=='POST':
        data= request.POST
        form = UserRegisterForm(data)
        if (form.is_valid()==True):
            form.save()
            #user= User.objects.get(username=username)
            print(form)
            return render(request, 'home.html')
        else:
            data= form.errors
            print(form.errors)
            return render(request, 'signUp.html', {"data": data})

def index(request):
    return render(request, 'signUp.html')

def index2(request):
    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return render(request,'home.html')

@login_required
def addQuestion(request):
    if request.method=='POST':
        data= request.POST
        #file= request.FILES
        form= QuestionForm(data)
        if (form.is_valid()==True):
            form.save()
            data="Question added"
            return render(request, 'home.html', {"data": data})
        else:
            form = QuestionForm()
            data= form.errors
            return render(request, 'index3.html', {'data':data})
    else:
        form = QuestionForm()
        return render(request, 'index3.html')

@login_required
def quiz(request, id):
    obj= Question.objects.all()
    next=id
    prev=id-1
    print(len(obj))
    if(next<=len(obj) and next>0 and prev>-1):
        queObj=Question.objects.filter(pk=id)
        print(queObj)
        queDict=queObj.values()
        print(queDict)
        que=queDict[0]['name']
        optionList=[queDict[0]['option1'], queDict[0]['option2'], queDict[0]['option3'], queDict[0]['option4']]
        correctAns= queDict[0]['ans']
        numberOfQue= [i for i in range(1, len(obj)+1)]
        next=next+1
    elif(next>len(obj)+1):
        next=0
        return render(request, 'home.html')
    elif(prev<0):
        prev=-1
        return render(request, 'home.html')
    elif(id==next):
        que=0
        optionList=0
        numberOfQue= None

    print("next="+ str(next))
    print("id:"+str(id))
    if request.method=='POST':
        data= request.POST
        currentUser=request.user
        userAns=data['ans']
        qObj=Question.objects.filter(pk=id-1).values()
        Q= Question.objects.get(pk=id-1)
        print(userAns)
        print(qObj[0]['ans'])
        dictAns={"A":qObj[0]['option1'], "B":qObj[0]['option2'],"C":qObj[0]['option3'],"D":qObj[0]['option4']}

        if(userAns== dictAns[qObj[0]['ans']]):
            answer= Answer(question=Q,user= currentUser, correct=True )
            answer.save()
            print("correct")
        elif(userAns!= qObj[0]['ans']):
            answer= Answer(question=Q,user= currentUser, correct=False)
            answer.save()
            print("incorrect")
    return render(request,'quiz.html', {"que": que, "optionList": optionList, "optionAlphaList": ["A", "B", "C", "D"] ,"numberOfQue": numberOfQue, "id": id, "next": next, "prev": prev})
@login_required
def report(request):
    obj= Question.objects.all()
    totalQue= len(obj)
    ans=Answer.objects.filter(user= request.user).order_by('-id')[:totalQue].values("correct")
    print(obj)
    print(totalQue)
    print(ans)
    ansList= [li['correct'] for li in ans]
    totalCorrAns= ansList.count(True)
    totalWrongAns= ansList.count(False)
    return render(request, 'report.html', {"totalCorrAns": totalCorrAns, "totalWrongAns": totalWrongAns, "totalQue": totalQue, "user": request.user})
@login_required
def userProfile(request):
    user=request.user
    username= user.username
    firstName= user.first_name
    lastName= user.last_name
    email= user.email
    return render(request, 'userProfile.html', {"user": user, "username": username, "firstName":firstName, "lastName": lastName, "email": email})
