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


class V1KubeVirtWorkloadUpdateStrategy(object):
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
        'batch_eviction_interval': 'K8sIoApimachineryPkgApisMetaV1Duration',
        'batch_eviction_size': 'int',
        'workload_update_methods': 'list[str]'
    }

    attribute_map = {
        'batch_eviction_interval': 'batchEvictionInterval',
        'batch_eviction_size': 'batchEvictionSize',
        'workload_update_methods': 'workloadUpdateMethods'
    }

    def __init__(self, batch_eviction_interval=None, batch_eviction_size=None, workload_update_methods=None):
        """
        V1KubeVirtWorkloadUpdateStrategy - a model defined in Swagger
        """

        self._batch_eviction_interval = None
        self._batch_eviction_size = None
        self._workload_update_methods = None

        if batch_eviction_interval is not None:
          self.batch_eviction_interval = batch_eviction_interval
        if batch_eviction_size is not None:
          self.batch_eviction_size = batch_eviction_size
        if workload_update_methods is not None:
          self.workload_update_methods = workload_update_methods

    @property
    def batch_eviction_interval(self):
        """
        Gets the batch_eviction_interval of this V1KubeVirtWorkloadUpdateStrategy.
        BatchEvictionInterval Represents the interval to wait before issuing the next batch of shutdowns  Defaults to 1 minute

        :return: The batch_eviction_interval of this V1KubeVirtWorkloadUpdateStrategy.
        :rtype: K8sIoApimachineryPkgApisMetaV1Duration
        """
        return self._batch_eviction_interval

    @batch_eviction_interval.setter
    def batch_eviction_interval(self, batch_eviction_interval):
        """
        Sets the batch_eviction_interval of this V1KubeVirtWorkloadUpdateStrategy.
        BatchEvictionInterval Represents the interval to wait before issuing the next batch of shutdowns  Defaults to 1 minute

        :param batch_eviction_interval: The batch_eviction_interval of this V1KubeVirtWorkloadUpdateStrategy.
        :type: K8sIoApimachineryPkgApisMetaV1Duration
        """

        self._batch_eviction_interval = batch_eviction_interval

    @property
    def batch_eviction_size(self):
        """
        Gets the batch_eviction_size of this V1KubeVirtWorkloadUpdateStrategy.
        BatchEvictionSize Represents the number of VMIs that can be forced updated per the BatchShutdownInteral interval  Defaults to 10

        :return: The batch_eviction_size of this V1KubeVirtWorkloadUpdateStrategy.
        :rtype: int
        """
        return self._batch_eviction_size

    @batch_eviction_size.setter
    def batch_eviction_size(self, batch_eviction_size):
        """
        Sets the batch_eviction_size of this V1KubeVirtWorkloadUpdateStrategy.
        BatchEvictionSize Represents the number of VMIs that can be forced updated per the BatchShutdownInteral interval  Defaults to 10

        :param batch_eviction_size: The batch_eviction_size of this V1KubeVirtWorkloadUpdateStrategy.
        :type: int
        """

        self._batch_eviction_size = batch_eviction_size

    @property
    def workload_update_methods(self):
        """
        Gets the workload_update_methods of this V1KubeVirtWorkloadUpdateStrategy.
        WorkloadUpdateMethods defines the methods that can be used to disrupt workloads during automated workload updates. When multiple methods are present, the least disruptive method takes precedence over more disruptive methods. For example if both LiveMigrate and Shutdown methods are listed, only VMs which are not live migratable will be restarted/shutdown  An empty list defaults to no automated workload updating

        :return: The workload_update_methods of this V1KubeVirtWorkloadUpdateStrategy.
        :rtype: list[str]
        """
        return self._workload_update_methods

    @workload_update_methods.setter
    def workload_update_methods(self, workload_update_methods):
        """
        Sets the workload_update_methods of this V1KubeVirtWorkloadUpdateStrategy.
        WorkloadUpdateMethods defines the methods that can be used to disrupt workloads during automated workload updates. When multiple methods are present, the least disruptive method takes precedence over more disruptive methods. For example if both LiveMigrate and Shutdown methods are listed, only VMs which are not live migratable will be restarted/shutdown  An empty list defaults to no automated workload updating

        :param workload_update_methods: The workload_update_methods of this V1KubeVirtWorkloadUpdateStrategy.
        :type: list[str]
        """

        self._workload_update_methods = workload_update_methods

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
        if not isinstance(other, V1KubeVirtWorkloadUpdateStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other