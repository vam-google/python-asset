# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.asset.v1p4beta1 AssetService API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.operation
import google.api_core.operations_v1
import grpc

from google.cloud.asset_v1p4beta1.gapic import asset_service_client_config
from google.cloud.asset_v1p4beta1.gapic import enums
from google.cloud.asset_v1p4beta1.gapic.transports import asset_service_grpc_transport
from google.cloud.asset_v1p4beta1.proto import asset_service_pb2
from google.cloud.asset_v1p4beta1.proto import asset_service_pb2_grpc
from google.longrunning import operations_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-asset").version


class AssetServiceClient(object):
    """Asset service definition."""

    SERVICE_ADDRESS = "cloudasset.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.asset.v1p4beta1.AssetService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AssetServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.AssetServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.AssetServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = asset_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=asset_service_grpc_transport.AssetServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = asset_service_grpc_transport.AssetServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def analyze_iam_policy(
        self,
        analysis_query,
        options_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        For extensions, this is the name of the type being extended. It is
        resolved in the same manner as type_name.

        Example:
            >>> from google.cloud import asset_v1p4beta1
            >>>
            >>> client = asset_v1p4beta1.AssetServiceClient()
            >>>
            >>> # TODO: Initialize `analysis_query`:
            >>> analysis_query = {}
            >>>
            >>> response = client.analyze_iam_policy(analysis_query)

        Args:
            analysis_query (Union[dict, ~google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery]): Required. The request query.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery`
            options_ (Union[dict, ~google.cloud.asset_v1p4beta1.types.Options]): Optional. The request options.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.asset_v1p4beta1.types.Options`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "analyze_iam_policy" not in self._inner_api_calls:
            self._inner_api_calls[
                "analyze_iam_policy"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.analyze_iam_policy,
                default_retry=self._method_configs["AnalyzeIamPolicy"].retry,
                default_timeout=self._method_configs["AnalyzeIamPolicy"].timeout,
                client_info=self._client_info,
            )

        request = asset_service_pb2.AnalyzeIamPolicyRequest(
            analysis_query=analysis_query, options=options_
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("analysis_query.parent", analysis_query.parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["analyze_iam_policy"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def export_iam_policy_analysis(
        self,
        analysis_query,
        output_config,
        options_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The normal response of the operation in case of success. If the
        original method returns no data on success, such as ``Delete``, the
        response is ``google.protobuf.Empty``. If the original method is
        standard ``Get``/``Create``/``Update``, the response should be the
        resource. For other methods, the response should have the type
        ``XxxResponse``, where ``Xxx`` is the original method name. For example,
        if the original method name is ``TakeSnapshot()``, the inferred response
        type is ``TakeSnapshotResponse``.

        Example:
            >>> from google.cloud import asset_v1p4beta1
            >>>
            >>> client = asset_v1p4beta1.AssetServiceClient()
            >>>
            >>> # TODO: Initialize `analysis_query`:
            >>> analysis_query = {}
            >>>
            >>> # TODO: Initialize `output_config`:
            >>> output_config = {}
            >>>
            >>> response = client.export_iam_policy_analysis(analysis_query, output_config)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            analysis_query (Union[dict, ~google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery]): Required. The request query.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisQuery`
            output_config (Union[dict, ~google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisOutputConfig]): Required. Output configuration indicating where the results will be output to.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisOutputConfig`
            options_ (Union[dict, ~google.cloud.asset_v1p4beta1.types.Options]): Optional. The request options.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.asset_v1p4beta1.types.Options`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.asset_v1p4beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "export_iam_policy_analysis" not in self._inner_api_calls:
            self._inner_api_calls[
                "export_iam_policy_analysis"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.export_iam_policy_analysis,
                default_retry=self._method_configs["ExportIamPolicyAnalysis"].retry,
                default_timeout=self._method_configs["ExportIamPolicyAnalysis"].timeout,
                client_info=self._client_info,
            )

        request = asset_service_pb2.ExportIamPolicyAnalysisRequest(
            analysis_query=analysis_query, output_config=output_config, options=options_
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("analysis_query.parent", analysis_query.parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["export_iam_policy_analysis"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            asset_service_pb2.ExportIamPolicyAnalysisResponse,
            metadata_type=asset_service_pb2.ExportIamPolicyAnalysisRequest,
        )
