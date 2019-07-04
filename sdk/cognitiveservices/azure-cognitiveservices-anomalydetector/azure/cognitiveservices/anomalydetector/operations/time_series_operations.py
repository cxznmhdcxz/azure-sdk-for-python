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

from msrest.pipeline import ClientRawResponse

from .. import models


class TimeSeriesOperations(object):
    """TimeSeriesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get(
            self, time_series_id, custom_headers=None, raw=False, **operation_config):
        """Get meta information of the specified timeseries.

        corresponds to create series, get series meta with timeseries id.

        :param time_series_id: Unique id for time series.
        :type time_series_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'timeSeriesId': self._serialize.url("time_series_id", time_series_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TimeSeries', response)
        if response.status_code == 404:
            deserialized = self._deserialize('APIError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/timeseries/{timeSeriesId}'}

    def create(
            self, time_series_id, body, custom_headers=None, raw=False, **operation_config):
        """Creat a timeseries.

        Create series, user need to provide timeSeriesId and granularity, if
        the series has dimension or name, description can be provided through
        the interface.

        :param time_series_id: Unique id for time series.
        :type time_series_id: str
        :param body:
        :type body:
         ~azure.cognitiveservices.anomalydetector.models.TimeSeriesCreateRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: APIError or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.anomalydetector.models.APIError or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'timeSeriesId': self._serialize.url("time_series_id", time_series_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'TimeSeriesCreateRequest')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201, 204, 409]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 409:
            deserialized = self._deserialize('APIError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/timeseries/{timeSeriesId}'}

    def delete(
            self, time_series_id, custom_headers=None, raw=False, **operation_config):
        """Delete the specified timeseries.

        Delete the specified timeseries.

        :param time_series_id: Unique id for time series.
        :type time_series_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'timeSeriesId': self._serialize.url("time_series_id", time_series_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/timeseries/{timeSeriesId}'}

    def list(
            self, next=None, custom_headers=None, raw=False, **operation_config):
        """List time series of each unique user.

        List time series of each unique user.

        :param next: Use "next" as query parameter to get next page data.
        :type next: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TimeSeriesList or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.anomalydetector.models.TimeSeriesList
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if next is not None:
            query_parameters['next'] = self._serialize.query("next", next, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TimeSeriesList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/timeseries'}

    def write(
            self, time_series_id, body, custom_headers=None, raw=False, **operation_config):
        """Insert or replace timeseries data for specified timeSeriesId. Note that
        this interface only stores data and do not detect these data.

        :param time_series_id: Unique id for time series.
        :type time_series_id: str
        :param body: Request body for writing timeseries.
        :type body:
         list[~azure.cognitiveservices.anomalydetector.models.Point]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: APIError or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.anomalydetector.models.APIError or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.write.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'timeSeriesId': self._serialize.url("time_series_id", time_series_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, '[Point]')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204, 404]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 404:
            deserialized = self._deserialize('APIError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    write.metadata = {'url': '/timeseries/{timeSeriesId}/write'}

    def detect_on_timestamp(
            self, time_series_id, body, custom_headers=None, raw=False, **operation_config):
        """Detect anomaly status on a given timestamp.

        This operation can be used in streaming monitoring scenario, when user
        would like to monitor a time series, the user only need to provide a
        time range, last detect API will check where last detection ends and
        will return detection results between last detection and the end time.

        :param time_series_id: Unique id for time series.
        :type time_series_id: str
        :param body: Timestamp is required in the request. Advanced model
         parameters (period, sensitivity, maxAnomalyRatio) can also be set in
         the request.
        :type body:
         ~azure.cognitiveservices.anomalydetector.models.AnomalyDetectOnTimestampRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.detect_on_timestamp.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'timeSeriesId': self._serialize.url("time_series_id", time_series_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'AnomalyDetectOnTimestampRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AnomalyDetectOnTimestampResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('APIError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_on_timestamp.metadata = {'url': '/timeseries/{timeSeriesId}/detect'}

    def change_point_detect_on_timestamp(
            self, time_series_id, body, custom_headers=None, raw=False, **operation_config):
        """Detect the closest change point before the given timestamp.

        Evaluate change point score before the given timestamp and give the
        closest change point.

        :param time_series_id: Unique id for time series.
        :type time_series_id: str
        :param body: Timestamp is needed. Advanced model parameters can also
         be set in the request if needed.
        :type body:
         ~azure.cognitiveservices.anomalydetector.models.ChangePointDetectOnTimestampRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.change_point_detect_on_timestamp.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'timeSeriesId': self._serialize.url("time_series_id", time_series_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'ChangePointDetectOnTimestampRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ChangePointDetectOnTimestampResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('APIError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    change_point_detect_on_timestamp.metadata = {'url': '/timeseries/{timeSeriesId}/changePoint/detect'}

    def label(
            self, time_series_id, body, custom_headers=None, raw=False, **operation_config):
        """Label API is used for users to label detection status of a certain time
        stamp of a time series.

        This operation is used for users to label Anomaly or ChangePoint states
        of a certain time stamp, these label will be used for regenerate
        detection model.

        :param time_series_id: Unique id for time series.
        :type time_series_id: str
        :param body: In Label request, user can set Anomaly|ChangePoint state
         (true, false, unknown) for a time range
        :type body:
         ~azure.cognitiveservices.anomalydetector.models.LabelRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: APIError or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.anomalydetector.models.APIError or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.label.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'timeSeriesId': self._serialize.url("time_series_id", time_series_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'LabelRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 404:
            deserialized = self._deserialize('APIError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    label.metadata = {'url': '/timeseries/{timeSeriesId}/label'}

    def query(
            self, time_series_id, body, custom_headers=None, raw=False, **operation_config):
        """Query timeseries with required field in each timestamp.

        :param time_series_id: Unique id for time series.
        :type time_series_id: str
        :param body: Request body for querying timeseries.
        :type body:
         ~azure.cognitiveservices.anomalydetector.models.TimeSeriesQueryRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.query.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'timeSeriesId': self._serialize.url("time_series_id", time_series_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'TimeSeriesQueryRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TimeSeriesQueryResponse', response)
        if response.status_code == 404:
            deserialized = self._deserialize('APIError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    query.metadata = {'url': '/timeseries/{timeSeriesId}/query'}

    def inconsistency_detect(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Detect inconsistent time series from a group of similar time series.

        This operation helps detect the inconsistent series among a group
        series with similar trend.

        :param body: Timestamp is necessary, and a parameter called epsilon is
         needed to tune the result. Epsilon should be within 0 and 1. A list of
         time series ids need to be provided to the service.
        :type body:
         ~azure.cognitiveservices.anomalydetector.models.InconsistencyDetectRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.inconsistency_detect.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'InconsistencyDetectRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Inconsistency', response)
        if response.status_code == 404:
            deserialized = self._deserialize('APIError', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    inconsistency_detect.metadata = {'url': '/timeseries/inconsistency/detect'}
