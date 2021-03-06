# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InnerHttpError(Model):
    """Object representing inner http error.

    :param status_code: HttpStatusCode from failed request
    :type status_code: int
    :param body: Body from failed request
    :type body: object
    """

    _attribute_map = {
        'status_code': {'key': 'statusCode', 'type': 'int'},
        'body': {'key': 'body', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(InnerHttpError, self).__init__(**kwargs)
        self.status_code = kwargs.get('status_code', None)
        self.body = kwargs.get('body', None)
