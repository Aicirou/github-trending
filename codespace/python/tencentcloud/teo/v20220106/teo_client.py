# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.teo.v20220106 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-01-06'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'


    def CreatePurgeTask(self, request):
        """创建清除缓存任务

        :param request: Request instance for CreatePurgeTask.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreatePurgeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePurgeTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePurgeTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePurgeTasks(self, request):
        """查询清除缓存历史记录

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)