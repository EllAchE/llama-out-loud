"use strict";
/* eslint-disable */
/* tslint:disable */
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.Api = exports.HttpClient = exports.ContentType = exports.CreateWebCallDTO = void 0;
class CreateWebCallDTO {
    /**
     * This is the assistant that will be used for the call. To use a transient assistant, use `assistant` instead.
     */
    assistantId;
    /**
     * Overrides for the assistant's settings and template variables.
     */
    assistantOverrides;
    /**
     * This is the assistant that will be used for the call. To use an existing assistant, use `assistantId` instead.
     */
    assistant;
    /**
     * This will expose SIP URI you can use to connect to the call. Disabled by default.
     */
    sipEnabled;
    /**
     * This is the metadata associated with the call.
     */
    metadata;
}
exports.CreateWebCallDTO = CreateWebCallDTO;
var ContentType;
(function (ContentType) {
    ContentType["Json"] = "application/json";
    ContentType["FormData"] = "multipart/form-data";
    ContentType["UrlEncoded"] = "application/x-www-form-urlencoded";
    ContentType["Text"] = "text/plain";
})(ContentType || (exports.ContentType = ContentType = {}));
class HttpClient {
    baseUrl = 'https://api.vapi.ai';
    securityData = null;
    securityWorker;
    abortControllers = new Map();
    customFetch = (...fetchParams) => fetch(...fetchParams);
    baseApiParams = {
        credentials: 'same-origin',
        headers: {},
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
    };
    constructor(apiConfig = {}) {
        Object.assign(this, apiConfig);
    }
    setSecurityData = (data) => {
        this.securityData = data;
    };
    encodeQueryParam(key, value) {
        const encodedKey = encodeURIComponent(key);
        return `${encodedKey}=${encodeURIComponent(typeof value === 'number' ? value : `${value}`)}`;
    }
    addQueryParam(query, key) {
        return this.encodeQueryParam(key, query[key]);
    }
    addArrayQueryParam(query, key) {
        const value = query[key];
        return value.map((v) => this.encodeQueryParam(key, v)).join('&');
    }
    toQueryString(rawQuery) {
        const query = rawQuery || {};
        const keys = Object.keys(query).filter((key) => 'undefined' !== typeof query[key]);
        return keys
            .map((key) => Array.isArray(query[key])
            ? this.addArrayQueryParam(query, key)
            : this.addQueryParam(query, key))
            .join('&');
    }
    addQueryParams(rawQuery) {
        const queryString = this.toQueryString(rawQuery);
        return queryString ? `?${queryString}` : '';
    }
    contentFormatters = {
        [ContentType.Json]: (input) => input !== null && (typeof input === 'object' || typeof input === 'string')
            ? JSON.stringify(input)
            : input,
        [ContentType.Text]: (input) => input !== null && typeof input !== 'string' ? JSON.stringify(input) : input,
        [ContentType.FormData]: (input) => Object.keys(input || {}).reduce((formData, key) => {
            const property = input[key];
            formData.append(key, property instanceof Blob
                ? property
                : typeof property === 'object' && property !== null
                    ? JSON.stringify(property)
                    : `${property}`);
            return formData;
        }, new FormData()),
        [ContentType.UrlEncoded]: (input) => this.toQueryString(input),
    };
    mergeRequestParams(params1, params2) {
        return {
            ...this.baseApiParams,
            ...params1,
            ...(params2 || {}),
            headers: {
                ...(this.baseApiParams.headers || {}),
                ...(params1.headers || {}),
                ...((params2 && params2.headers) || {}),
            },
        };
    }
    createAbortSignal = (cancelToken) => {
        if (this.abortControllers.has(cancelToken)) {
            const abortController = this.abortControllers.get(cancelToken);
            if (abortController) {
                return abortController.signal;
            }
            return void 0;
        }
        const abortController = new AbortController();
        this.abortControllers.set(cancelToken, abortController);
        return abortController.signal;
    };
    abortRequest = (cancelToken) => {
        const abortController = this.abortControllers.get(cancelToken);
        if (abortController) {
            abortController.abort();
            this.abortControllers.delete(cancelToken);
        }
    };
    request = async ({ body, secure, path, type, query, format, baseUrl, cancelToken, ...params }) => {
        const secureParams = ((typeof secure === 'boolean' ? secure : this.baseApiParams.secure) &&
            this.securityWorker &&
            (await this.securityWorker(this.securityData))) ||
            {};
        const requestParams = this.mergeRequestParams(params, secureParams);
        const queryString = query && this.toQueryString(query);
        const payloadFormatter = this.contentFormatters[type || ContentType.Json];
        const responseFormat = format || requestParams.format;
        return this.customFetch(`${baseUrl || this.baseUrl || ''}${path}${queryString ? `?${queryString}` : ''}`, {
            ...requestParams,
            headers: {
                ...(requestParams.headers || {}),
                ...(type && type !== ContentType.FormData ? { 'Content-Type': type } : {}),
            },
            signal: (cancelToken ? this.createAbortSignal(cancelToken) : requestParams.signal) || null,
            body: typeof body === 'undefined' || body === null ? null : payloadFormatter(body),
        }).then(async (response) => {
            const r = response;
            r.data = null;
            r.error = null;
            const data = !responseFormat
                ? r
                : await response[responseFormat]()
                    .then((data) => {
                    if (r.ok) {
                        r.data = data;
                    }
                    else {
                        r.error = data;
                    }
                    return r;
                })
                    .catch((e) => {
                    r.error = e;
                    return r;
                });
            if (cancelToken) {
                this.abortControllers.delete(cancelToken);
            }
            if (!response.ok)
                throw data;
            return data;
        });
    };
}
exports.HttpClient = HttpClient;
/**
 * @title Vapi API
 * @version 1.0
 * @baseUrl https://api.vapi.ai
 * @contact
 *
 * API for building voice assistants
 */
class Api extends HttpClient {
    assistant = {
        /**
         * No description
         *
         * @tags Assistants
         * @name AssistantControllerCreate
         * @summary Create Assistant
         * @request POST:/assistant
         * @secure
         */
        assistantControllerCreate: (data, params = {}) => this.request({
            path: `/assistant`,
            method: 'POST',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Assistants
         * @name AssistantControllerFindAll
         * @summary List Assistants
         * @request GET:/assistant
         * @secure
         */
        assistantControllerFindAll: (query, params = {}) => this.request({
            path: `/assistant`,
            method: 'GET',
            query: query,
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Assistants
         * @name AssistantControllerFindOne
         * @summary Get Assistant
         * @request GET:/assistant/{id}
         * @secure
         */
        assistantControllerFindOne: (id, params = {}) => this.request({
            path: `/assistant/${id}`,
            method: 'GET',
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Assistants
         * @name AssistantControllerUpdate
         * @summary Update Assistant
         * @request PATCH:/assistant/{id}
         * @secure
         */
        assistantControllerUpdate: (id, data, params = {}) => this.request({
            path: `/assistant/${id}`,
            method: 'PATCH',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Assistants
         * @name AssistantControllerReplace
         * @summary Replace Assistant
         * @request PUT:/assistant/{id}
         * @secure
         */
        assistantControllerReplace: (id, data, params = {}) => this.request({
            path: `/assistant/${id}`,
            method: 'PUT',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Assistants
         * @name AssistantControllerRemove
         * @summary Delete Assistant
         * @request DELETE:/assistant/{id}
         * @secure
         */
        assistantControllerRemove: (id, params = {}) => this.request({
            path: `/assistant/${id}`,
            method: 'DELETE',
            secure: true,
            format: 'json',
            ...params,
        }),
    };
    call = {
        /**
         * No description
         *
         * @tags Calls
         * @name CallControllerFindAll
         * @summary List Calls
         * @request GET:/call
         * @secure
         */
        callControllerFindAll: (query, params = {}) => this.request({
            path: `/call`,
            method: 'GET',
            query: query,
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Calls
         * @name CallControllerFindOne
         * @summary Get Call
         * @request GET:/call/{id}
         * @secure
         */
        callControllerFindOne: (id, params = {}) => this.request({
            path: `/call/${id}`,
            method: 'GET',
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Calls
         * @name CallControllerCreatePhoneCall
         * @summary Create Phone Call
         * @request POST:/call/phone
         * @secure
         */
        callControllerCreatePhoneCall: (data, params = {}) => this.request({
            path: `/call/phone`,
            method: 'POST',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Calls
         * @name CallControllerCreateWebCall
         * @summary Create Web Call
         * @request POST:/call/web
         * @secure
         */
        callControllerCreateWebCall: (data, params = {}) => this.request({
            path: `/call/web`,
            method: 'POST',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
    };
    credential = {
        /**
         * No description
         *
         * @tags Credentials
         * @name CredentialControllerCreate
         * @summary Create Credential
         * @request POST:/credential
         * @secure
         */
        credentialControllerCreate: (data, params = {}) => this.request({
            path: `/credential`,
            method: 'POST',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Credentials
         * @name CredentialControllerFindAll
         * @summary List Credentials
         * @request GET:/credential
         * @secure
         */
        credentialControllerFindAll: (query, params = {}) => this.request({
            path: `/credential`,
            method: 'GET',
            query: query,
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Credentials
         * @name CredentialControllerFindOne
         * @summary Get Credential
         * @request GET:/credential/{id}
         * @secure
         */
        credentialControllerFindOne: (id, params = {}) => this.request({
            path: `/credential/${id}`,
            method: 'GET',
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Credentials
         * @name CredentialControllerUpdate
         * @summary Update Credential
         * @request PUT:/credential/{id}
         * @secure
         */
        credentialControllerUpdate: (id, data, params = {}) => this.request({
            path: `/credential/${id}`,
            method: 'PUT',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Credentials
         * @name CredentialControllerRemove
         * @summary Delete Credential
         * @request DELETE:/credential/{id}
         * @secure
         */
        credentialControllerRemove: (id, params = {}) => this.request({
            path: `/credential/${id}`,
            method: 'DELETE',
            secure: true,
            format: 'json',
            ...params,
        }),
    };
    phoneNumber = {
        /**
         * No description
         *
         * @tags Phone Numbers
         * @name PhoneNumberControllerBuy
         * @summary Buy Phone Number
         * @request POST:/phone-number/buy
         * @secure
         */
        phoneNumberControllerBuy: (data, params = {}) => this.request({
            path: `/phone-number/buy`,
            method: 'POST',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Phone Numbers
         * @name PhoneNumberControllerImportTwilio
         * @summary Import Twilio Number
         * @request POST:/phone-number/import/twilio
         * @secure
         */
        phoneNumberControllerImportTwilio: (data, params = {}) => this.request({
            path: `/phone-number/import/twilio`,
            method: 'POST',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Phone Numbers
         * @name PhoneNumberControllerImportVonage
         * @summary Import Vonage Number
         * @request POST:/phone-number/import/vonage
         * @secure
         */
        phoneNumberControllerImportVonage: (data, params = {}) => this.request({
            path: `/phone-number/import/vonage`,
            method: 'POST',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Phone Numbers
         * @name PhoneNumberControllerFindAll
         * @summary List Phone Numbers
         * @request GET:/phone-number
         * @secure
         */
        phoneNumberControllerFindAll: (query, params = {}) => this.request({
            path: `/phone-number`,
            method: 'GET',
            query: query,
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Phone Numbers
         * @name PhoneNumberControllerFindOne
         * @summary Get Phone Number
         * @request GET:/phone-number/{id}
         * @secure
         */
        phoneNumberControllerFindOne: (id, params = {}) => this.request({
            path: `/phone-number/${id}`,
            method: 'GET',
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Phone Numbers
         * @name PhoneNumberControllerUpdate
         * @summary Update Phone Number
         * @request PATCH:/phone-number/{id}
         * @secure
         */
        phoneNumberControllerUpdate: (id, data, params = {}) => this.request({
            path: `/phone-number/${id}`,
            method: 'PATCH',
            body: data,
            secure: true,
            type: ContentType.Json,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Phone Numbers
         * @name PhoneNumberControllerRemove
         * @summary Delete Phone Number
         * @request DELETE:/phone-number/{id}
         * @secure
         */
        phoneNumberControllerRemove: (id, params = {}) => this.request({
            path: `/phone-number/${id}`,
            method: 'DELETE',
            secure: true,
            format: 'json',
            ...params,
        }),
    };
    metrics = {
        /**
         * No description
         *
         * @tags Metrics
         * @name MetricsControllerFindAll
         * @summary List Metrics
         * @request GET:/metrics
         * @secure
         */
        metricsControllerFindAll: (query, params = {}) => this.request({
            path: `/metrics`,
            method: 'GET',
            query: query,
            secure: true,
            format: 'json',
            ...params,
        }),
    };
    voiceLibrary = {
        /**
         * No description
         *
         * @tags Voice Library
         * @name VoiceLibraryControllerVoiceGetByProvider
         * @summary Get voices in Voice Library by Providers
         * @request GET:/voice-library/{provider}
         * @secure
         */
        voiceLibraryControllerVoiceGetByProvider: (provider, params = {}) => this.request({
            path: `/voice-library/${provider}`,
            method: 'GET',
            secure: true,
            format: 'json',
            ...params,
        }),
        /**
         * No description
         *
         * @tags Voice Library
         * @name VoiceLibraryControllerVoiceLibrarySyncByProvider
         * @summary Sync voices in Voice Library by Providers
         * @request POST:/voice-library/sync/{provider}
         * @secure
         */
        voiceLibraryControllerVoiceLibrarySyncByProvider: (provider, params = {}) => this.request({
            path: `/voice-library/sync/${provider}`,
            method: 'POST',
            secure: true,
            format: 'json',
            ...params,
        }),
    };
    logging = {
        /**
         * No description
         *
         * @tags Logging
         * @name LoggingControllerGetLogs
         * @summary Get Logging Logs
         * @request GET:/logging
         * @secure
         */
        loggingControllerGetLogs: (query, params = {}) => this.request({
            path: `/logging`,
            method: 'GET',
            query: query,
            secure: true,
            format: 'json',
            ...params,
        }),
    };
}
exports.Api = Api;
