import numpy as np
from openvino.runtime import Core

core = Core() 
model = core.read_model('googlenet-v2.xml') 
compiled_model = core.compile_model(model, 'CPU') 
infer_request = compiled_model.create_infer_request() 

input_tensor = np.zeros((1,3,224,224))

infer_request.infer({0: input_tensor}) 
res = infer_request.get_tensor('prob').data 

res = res.ravel()
idx = np.argsort(res)[::-1]
for i in range(5):
    print(idx[i]+1, res[idx[i]])
