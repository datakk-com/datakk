class mydolphindb:

  def __init__(self,host='localhost',port=8848,user='admin',word='123456'):
    from dolphindb import session
    self.ss = ss = session()
    rt = ss.connect(host, port, user, word)
    assert rt is True, 'login failed'

  def __call__(self,*args,**kwargs): return self.ss.run(*args,**kwargs)
  def __getattr__(self,k): return getattr(self.ss,k)

