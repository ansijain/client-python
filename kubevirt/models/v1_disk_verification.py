# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DiskVerification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'memory_limit': 'K8sIoApimachineryPkgApiResourceQuantity'
    }

    attribute_map = {
        'memory_limit': 'memoryLimit'
    }

    def __init__(self, memory_limit=None):
        """
        V1DiskVerification - a model defined in Swagger
        """

        self._memory_limit = None

        self.memory_limit = memory_limit

    @property
    def memory_limit(self):
        """
        Gets the memory_limit of this V1DiskVerification.

        :return: The memory_limit of this V1DiskVerification.
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        """
        Sets the memory_limit of this V1DiskVerification.

        :param memory_limit: The memory_limit of this V1DiskVerification.
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """
        if memory_limit is None:
            raise ValueError("Invalid value for `memory_limit`, must not be `None`")

        self._memory_limit = memory_limit

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1DiskVerification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other