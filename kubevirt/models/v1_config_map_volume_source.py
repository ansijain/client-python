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


class V1ConfigMapVolumeSource(object):
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
        'name': 'str',
        'optional': 'bool',
        'volume_label': 'str'
    }

    attribute_map = {
        'name': 'name',
        'optional': 'optional',
        'volume_label': 'volumeLabel'
    }

    def __init__(self, name=None, optional=None, volume_label=None):
        """
        V1ConfigMapVolumeSource - a model defined in Swagger
        """

        self._name = None
        self._optional = None
        self._volume_label = None

        if name is not None:
          self.name = name
        if optional is not None:
          self.optional = optional
        if volume_label is not None:
          self.volume_label = volume_label

    @property
    def name(self):
        """
        Gets the name of this V1ConfigMapVolumeSource.
        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :return: The name of this V1ConfigMapVolumeSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ConfigMapVolumeSource.
        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :param name: The name of this V1ConfigMapVolumeSource.
        :type: str
        """

        self._name = name

    @property
    def optional(self):
        """
        Gets the optional of this V1ConfigMapVolumeSource.
        Specify whether the ConfigMap or it's keys must be defined +optional

        :return: The optional of this V1ConfigMapVolumeSource.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """
        Sets the optional of this V1ConfigMapVolumeSource.
        Specify whether the ConfigMap or it's keys must be defined +optional

        :param optional: The optional of this V1ConfigMapVolumeSource.
        :type: bool
        """

        self._optional = optional

    @property
    def volume_label(self):
        """
        Gets the volume_label of this V1ConfigMapVolumeSource.
        The volume label of the resulting disk inside the VMI. Different bootstrapping mechanisms require different values. Typical values are \"cidata\" (cloud-init), \"config-2\" (cloud-init) or \"OEMDRV\" (kickstart). +optional

        :return: The volume_label of this V1ConfigMapVolumeSource.
        :rtype: str
        """
        return self._volume_label

    @volume_label.setter
    def volume_label(self, volume_label):
        """
        Sets the volume_label of this V1ConfigMapVolumeSource.
        The volume label of the resulting disk inside the VMI. Different bootstrapping mechanisms require different values. Typical values are \"cidata\" (cloud-init), \"config-2\" (cloud-init) or \"OEMDRV\" (kickstart). +optional

        :param volume_label: The volume_label of this V1ConfigMapVolumeSource.
        :type: str
        """

        self._volume_label = volume_label

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
        if not isinstance(other, V1ConfigMapVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
