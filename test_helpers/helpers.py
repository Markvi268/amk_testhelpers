   # -*- coding: utf-8 -*-
import sys
import subprocess
import re
import os
import shutil
import glob
import threading



def getpath():
    # Find path to current root
    pathlist = split(sys.argv[0])
    if len(pathlist) == 1:
        path = './'
    else:
        path = pathlist[0] + '/'
    return path

def callpythoncode(code, cmdline_args=[], input='', timeout=30):
    path=getpath()

    testcodefile='tests/my_test_code.py'
    f=open(testcodefile, "w")
    f.write(code)
    f.close()
    
    cmd_line=[sys.executable, '../'+testcodefile,]+cmdline_args
    try:
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except subprocess.TimeoutExpired:
        print('Timeout expired!')
        return ''
    except:
        print('Execute dropped to fallback!')
        cmd_line_str=' '.join(cmd_line)
        rc = subprocess.run(cmd_line_str, cwd=path+'/src', stdout=subprocess.PIPE, universal_newlines=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    os.remove(testcodefile)    
    
    return rc.stdout

#Run my_code.py and additional code
def callpythonmaincode(code, cmdline_args=[], input='', timeout=30):
    my_code=loadmycode()

    return callpythoncode(code=my_code+code, cmdline_args=cmdline_args, input=input, timeout=timeout)

#Load student code
def loadmycode(codefile='src/my_code.py'):
    for encoding in ['latin1', 'utf8','utf16','cp437']:
        try:
            with open(codefile, encoding=encoding) as f:
                my_code = f.read()
            return my_code
        except:
            pass

#Run my_code.py
def callpython(cmdline_args=[], input='', timeout=30):
    path=getpath()

    cmd_line=[sys.executable, 'my_code.py',]+cmdline_args
    try:
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except subprocess.TimeoutExpired:
        print('Timeout expired!')
        return ''
    except:
        print('Execute dropped to fallback!')
        cmd_line_str=' '.join(cmd_line)
        print('"',cmd_line_str, '"')
        rc = subprocess.run(cmd_line_str, cwd=path+'/src', stdout=subprocess.PIPE, universal_newlines=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout



#Run my_code.py in separate thread
def callpython_subprocess(cmdline_args=[], input='', timeout=30):
    th=threading.Thread(target=callpython, args=(cmdline_args, input, timeout))
    th.start()
    return th

def load_python_code():
    file_name=getpath()+'/src/my_code.py'
    with open(file_name) as f:
        contents = f.read()
        return contents
    
def dotNetProjectName():
    project_files=glob.glob('*.csproj')
    project_file=project_files[0]
    return os.path.splitext(project_file)[0]


def dotNetNumbersFormat():
    path=getpath()+'/../test_helpers'
    project_name='environment'

    tmp_directories=['bin', 'obj']
    for d in tmp_directories:
        try:
            shutil.rmtree(path+'/'+d)
        except:
            pass

    timeout=10
        
    try:
        rc = subprocess.run(['dotnet', 'build'], cwd=path, shell=True)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Compile falled to fallback!!')
        rc = subprocess.run(['dotnet build'], cwd=path, shell=True)
        print("Fallback completed, don't worry")

    try:
        cmd_line=[path+'/bin/Debug/net6.0/'+project_name+'.exe',]
        rc = subprocess.run(cmd_line, cwd=path, stdout=subprocess.PIPE, text=True, timeout=timeout)
    except:
        print('!!Running falled to fallback!!')
        cmd_line=[path+'/bin/Debug/net6.0/'+project_name,]
        rc = subprocess.run(cmd_line, stdout=subprocess.PIPE, text=True, timeout=timeout)
        print("Fallback completed, don't worry")

    neg=rc.stdout[0]
    sep=rc.stdout[2]
    return neg, sep


def callDotNet(cmdline_args=[], input='', timeout=30, build=True):
    path=getpath()
    project_name=dotNetProjectName()

    tmp_directories=['bin', 'obj']
    if build:
        for d in tmp_directories:
            try:
                shutil.rmtree(d)
            except:
                pass
    
    #Compile the source code
    #shutil.copy2('tests/my_code.csproj', 'src/my_code.csproj')
    if build:
        try:
            rc = subprocess.run(['dotnet', 'build'], cwd=path, shell=True)
            if rc.returncode!=0:
                raise FileNotFoundError
        except:
            print('!!Compile falled to fallback!!')
            rc = subprocess.run(['dotnet build'], cwd=path, shell=True)
            print("Fallback completed, don't worry")

    try:
        cmd_line=['bin/Debug/net6.0/'+project_name+'.exe',]+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except:
        print('!!Running falled to fallback!!')
        cmd_line=['../bin/Debug/net6.0/'+project_name,]+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout

def callDotNetFunction(cmdline_args=[], input='', timeout=30, build=True):
    path=getpath()
    project_name=dotNetProjectName()

    tmp_directories=['bin', 'obj']
    if build:
        for d in tmp_directories:
            try:
                shutil.rmtree(d)
            except:
                pass

    #shutil.copy2('tests/testmain.cs', 'src/testmain.cs')
    #shutil.copy2('tests/my_code.csproj', 'src/my_code.csproj')
    #Compile the source code
    if build:
        if os.path.exists('tests/testmain.cs.hidden'):
            shutil.copyfile('tests/testmain.cs.hidden', 'tests/testmain.cs')
        try:
            rc = subprocess.run(['dotnet', 'build'], cwd=path, shell=True)
            if rc.returncode!=0:
                raise FileNotFoundError
        except:
            print('!!Compile falled to fallback!!')
            rc = subprocess.run(['dotnet build'], cwd=path, shell=True)
            print("Fallback completed, don't worry")
        finally:
            if os.path.exists('tests/testmain.cs.hidden'):
                os.remove('tests/testmain.cs')


    try:
        cmd_line=['bin/Debug/net6.0/'+project_name+'.exe',]+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except:
        print('!!Running falled to fallback!!')
        cmd_line=['../bin/Debug/net6.0/'+project_name,]+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout

def callMono(cmdline_args=[], input='', timeout=30):
    path=getpath()

    #Compile the source code
    try:
        rc = subprocess.run(['mcs', 'my_code.cs'], cwd=path+'/src', shell=True)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Compile falled to fallback!!')
        rc = subprocess.run(['mcs my_code.cs'], cwd=path+'/src', shell=True)
        print("Fallback completed, don't worry")

    cmd_line=['mono','my_code.exe',]+cmdline_args
    rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)

    return rc.stdout

def callMonoFunction(cmdline_args=[], input='', timeout=30):
    path=getpath()

    #Compile the source code
    try:
        rc = subprocess.run(['mcs', '../tests/testmain.cs', 'my_code.cs'], cwd=path+'/src', shell=True)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Compile falled to fallback!!')
        rc = subprocess.run(['mcs ../tests/testmain.cs my_code.cs'], cwd=path+'/src', shell=True)
        print("Fallback completed, don't worry")

    cmd_line=['mono','../tests/testmain.exe',]+cmdline_args
    rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)

    return rc.stdout

def callCPP(cmdline_args=[], input='', timeout=30, compiler='g++', enable_VS=True):
    return callC(cmdline_args, input, timeout, compiler, 'my_code.cpp', enable_VS)

def callC(cmdline_args=[], input='', timeout=30, compiler='gcc', source='my_code.c', enable_VS=True):
    path=getpath()

    #Compile the source code
    VS_compile_succeed=False
    if enable_VS:
        try:
            rc = subprocess.run(['cl.exe', source], cwd=path+'/src', shell=True)
            if rc.returncode!=0:
                raise FileNotFoundError
            VS_compile_succeed=True
        except:
            print('Visual Studio compile failed, trying GCC!')
    
    if not VS_compile_succeed:
        try:
            rc = subprocess.run([compiler,source,'-o','my_code.exe'], cwd=path+'/src', shell=True)
            if rc.returncode!=0:
                raise FileNotFoundError
        except:
            print('!!Compile dropped to fallback!!')
            rc = subprocess.run([compiler+' '+source+' -o my_code.exe'], cwd=path+'/src', shell=True)
            print("Fallback completed, don't worry")


    try:
        cmd_line=['./my_code.exe']+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Running dropped to fallback!!')
        cmd_line=[path+'\\src\\my_code.exe']+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout

def callCPPFunction(cmdline_args=[], input='', timeout=30, compiler='g++', source='my_code.cpp', testmain='../tests/testmain.cpp', enable_VS=True):
    return callCFunction(cmdline_args, input, timeout, compiler, source, testmain, enable_VS)


def callCFunction(cmdline_args=[], input='', timeout=30, compiler='gcc', source='my_code.c', testmain='../tests/testmain.c', enable_VS=True):
    path=getpath()

    #Compile the source code
    VS_compile_succeed=False
    if enable_VS:
        try:
            rc = subprocess.run(['cl.exe', source, testmain, '/DCLIBRARYTEST'], cwd=path+'/src', shell=True)
            if rc.returncode!=0:
                raise FileNotFoundError
            VS_compile_succeed=True
        except:
            print('Visual Studio compile failed, trying GCC!')
    
    if not VS_compile_succeed:
        try:
            rc = subprocess.run([compiler, source, testmain, '-o', 'my_code.exe', '-D', 'CLIBRARYTEST'], cwd=path+'/src', shell=True)
            if rc.returncode!=0:
                raise FileNotFoundError
        except:
            print('!!Compile dropped to fallback!!')
            rc = subprocess.run([compiler+' '+source+' '+testmain+' -o my_code.exe -DCLIBRARYTEST'], cwd=path+'/src', shell=True)
            print("Fallback completed, don't worry")


    try:
        cmd_line=['./my_code.exe']+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Running dropped to fallback!!')
        cmd_line=[path+'\\src\\my_code.exe']+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout

def split(s):
    return re.split('/|\\\\', s)