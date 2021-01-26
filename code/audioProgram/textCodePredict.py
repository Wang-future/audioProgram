# coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from oauth2client.client import GoogleCredentials
from six.moves import input  # pylint: disable=redefined-builtin

from tensor2tensor import problems as problems_lib  # pylint: disable=unused-import
from tensor2tensor.serving import serving_utils
from tensor2tensor.utils import registry
from tensor2tensor.utils import usr_dir
import tensorflow as tf

def make_request_fn(server_name, server_address):
    """Returns a request function."""
    request_fn = serving_utils.make_grpc_request_fn(
        servable_name=server_name,
        server=server_address,
        timeout_secs=10)
    return request_fn


# def query_t2t(input_txt, data_dir, problem_name, server_name, server_address, t2t_usr_dir):
#     usr_dir.import_usr_dir(t2t_usr_dir)
#     problem = registry.problem(problem_name)
#     hparams = tf.contrib.training.HParams(
#         data_dir=os.path.expanduser(data_dir))
#     problem.get_hparams(hparams)
#     request_fn = make_request_fn(server_name, server_address)
#     inputs = input_txt
#     outputs = serving_utils.predict([inputs], problem, request_fn)
#     output, score = outputs[0]
#     return output, score
class TextCodePredict:
    def __init__(self):
        self.data_dir = "/data/project/audioProgram/code/audioProgram/transformerModel/selfTrain/data"
        self.problem_name = "my_problem"
        self.t2t_usr_dir = "/data/project/audioProgram/code/audioProgram/transformerModel/selfTrain"
        self.server_name = "text2code_model"
        self.server_address = "172.17.0.39:8500"

    def query_t2t(self, input_txt, data_dir, problem_name, server_name, server_address, t2t_usr_dir):
        usr_dir.import_usr_dir(t2t_usr_dir)
        problem = registry.problem(problem_name)
        hparams = tf.contrib.training.HParams(
            data_dir=os.path.expanduser(data_dir))
        problem.get_hparams(hparams)
        request_fn = make_request_fn(server_name, server_address)
        inputs = input_txt
        outputs = serving_utils.predict([inputs], problem, request_fn)
        output, score = outputs[0]
        return output, score

    def textCode(self, input_text, seqId = ""):
        ret_data = {}
        ret_data['ret_code'] = 0
        ret_data['seqId'] = seqId
        try:
            output, score = self.query_t2t(input_text, self.data_dir, self.problem_name, self.server_name, self.server_address, self.t2t_usr_dir)
            ret_data['text'] = str(output).replace('<EOS>','').replace('<pad>','')#去掉填充
            ret_data['ret_code'] = 1
        except Exception as e:
            ret_data['ret_code'] = 2
            ret_data['text'] = "seqId:" + seqId + ", 预测出错,原因:"+str(e)
        return ret_data

if __name__ == "__main__":
    myTextCodePredict = TextCodePredict()
    data_dir="/data/project/audioProgram/code/audioProgram/transformerModel/selfTrain/data"
    problem_name = "my_problem"
    t2t_usr_dir = "/data/project/audioProgram/code/audioProgram/transformerModel/selfTrain"
    server_name = "text2code_model"
    server_address = "172.17.0.39:8500"#"http://172.17.0.39:8501/v1/models/text2code_model:predict"#"172.17.0.39:8501"
    input_text = "检查列表“myList”中的所有元素是否相同"
    output, score = myTextCodePredict.query_t2t(input_text, data_dir, problem_name, server_name, server_address, t2t_usr_dir)
    ret_data = myTextCodePredict.textCode(input_text,"fsdk")
    print(str(output))
    print(ret_data['text'])
