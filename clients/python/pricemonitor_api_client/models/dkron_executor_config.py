# coding: utf-8

"""
    Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts, and more.  This API supports both public endpoints for customer integration and internal endpoints for platform management. All endpoints are authenticated using either Basic Authentication or JWT Bearer tokens.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.7216
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pricemonitor_api_client.configuration import Configuration


class DkronExecutorConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'method': 'str',
        'url': 'str',
        'headers': 'str',
        'body': 'str',
        'timeout': 'str',
        'expect_code': 'str',
        'expect_body': 'str',
        'debug': 'str'
    }

    attribute_map = {
        'method': 'method',
        'url': 'url',
        'headers': 'headers',
        'body': 'body',
        'timeout': 'timeout',
        'expect_code': 'expectCode',
        'expect_body': 'expectBody',
        'debug': 'debug'
    }

    def __init__(self, method=None, url=None, headers=None, body=None, timeout=None, expect_code=None, expect_body=None, debug=None, local_vars_configuration=None):  # noqa: E501
        """DkronExecutorConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._method = None
        self._url = None
        self._headers = None
        self._body = None
        self._timeout = None
        self._expect_code = None
        self._expect_body = None
        self._debug = None
        self.discriminator = None

        if method is not None:
            self.method = method
        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers
        if body is not None:
            self.body = body
        if timeout is not None:
            self.timeout = timeout
        if expect_code is not None:
            self.expect_code = expect_code
        if expect_body is not None:
            self.expect_body = expect_body
        if debug is not None:
            self.debug = debug

    @property
    def method(self):
        """Gets the method of this DkronExecutorConfig.  # noqa: E501

        Request method in uppercase  # noqa: E501

        :return: The method of this DkronExecutorConfig.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this DkronExecutorConfig.

        Request method in uppercase  # noqa: E501

        :param method: The method of this DkronExecutorConfig.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def url(self):
        """Gets the url of this DkronExecutorConfig.  # noqa: E501

        Request url  # noqa: E501

        :return: The url of this DkronExecutorConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DkronExecutorConfig.

        Request url  # noqa: E501

        :param url: The url of this DkronExecutorConfig.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this DkronExecutorConfig.  # noqa: E501

        Json string, such as \"[\"Content-Type: application/json\"]\"  # noqa: E501

        :return: The headers of this DkronExecutorConfig.  # noqa: E501
        :rtype: str
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this DkronExecutorConfig.

        Json string, such as \"[\"Content-Type: application/json\"]\"  # noqa: E501

        :param headers: The headers of this DkronExecutorConfig.  # noqa: E501
        :type: str
        """

        self._headers = headers

    @property
    def body(self):
        """Gets the body of this DkronExecutorConfig.  # noqa: E501

        POST body  # noqa: E501

        :return: The body of this DkronExecutorConfig.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DkronExecutorConfig.

        POST body  # noqa: E501

        :param body: The body of this DkronExecutorConfig.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def timeout(self):
        """Gets the timeout of this DkronExecutorConfig.  # noqa: E501

        Request timeout, unit seconds  # noqa: E501

        :return: The timeout of this DkronExecutorConfig.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this DkronExecutorConfig.

        Request timeout, unit seconds  # noqa: E501

        :param timeout: The timeout of this DkronExecutorConfig.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def expect_code(self):
        """Gets the expect_code of this DkronExecutorConfig.  # noqa: E501

        Expect response code, such as 200,206  # noqa: E501

        :return: The expect_code of this DkronExecutorConfig.  # noqa: E501
        :rtype: str
        """
        return self._expect_code

    @expect_code.setter
    def expect_code(self, expect_code):
        """Sets the expect_code of this DkronExecutorConfig.

        Expect response code, such as 200,206  # noqa: E501

        :param expect_code: The expect_code of this DkronExecutorConfig.  # noqa: E501
        :type: str
        """

        self._expect_code = expect_code

    @property
    def expect_body(self):
        """Gets the expect_body of this DkronExecutorConfig.  # noqa: E501

        Expect response body, support regexp, such as /success/  # noqa: E501

        :return: The expect_body of this DkronExecutorConfig.  # noqa: E501
        :rtype: str
        """
        return self._expect_body

    @expect_body.setter
    def expect_body(self, expect_body):
        """Sets the expect_body of this DkronExecutorConfig.

        Expect response body, support regexp, such as /success/  # noqa: E501

        :param expect_body: The expect_body of this DkronExecutorConfig.  # noqa: E501
        :type: str
        """

        self._expect_body = expect_body

    @property
    def debug(self):
        """Gets the debug of this DkronExecutorConfig.  # noqa: E501

        Debug option, will log everything when this option is not empty  # noqa: E501

        :return: The debug of this DkronExecutorConfig.  # noqa: E501
        :rtype: str
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this DkronExecutorConfig.

        Debug option, will log everything when this option is not empty  # noqa: E501

        :param debug: The debug of this DkronExecutorConfig.  # noqa: E501
        :type: str
        """

        self._debug = debug

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DkronExecutorConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DkronExecutorConfig):
            return True

        return self.to_dict() != other.to_dict()
