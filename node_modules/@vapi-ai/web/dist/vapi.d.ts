/// <reference types="node" />
import { Call, CreateAssistantDTO, OverrideAssistantDTO } from './api';
import type { ChatCompletionMessageParam } from 'openai/resources';
import EventEmitter from 'events';
export interface AddMessageMessage {
    type: 'add-message';
    message: ChatCompletionMessageParam;
}
export interface ControlMessages {
    type: 'control';
    control: 'mute-assistant' | 'unmute-assistant';
}
type VapiClientToServerMessage = AddMessageMessage | ControlMessages;
type VapiEventNames = 'call-end' | 'call-start' | 'volume-level' | 'speech-start' | 'speech-end' | 'message' | 'error';
type VapiEventListeners = {
    'call-end': () => void;
    'call-start': () => void;
    'volume-level': (volume: number) => void;
    'speech-start': () => void;
    'speech-end': () => void;
    message: (message: any) => void;
    error: (error: any) => void;
};
declare class VapiEventEmitter extends EventEmitter {
    on<E extends VapiEventNames>(event: E, listener: VapiEventListeners[E]): this;
    once<E extends VapiEventNames>(event: E, listener: VapiEventListeners[E]): this;
    emit<E extends VapiEventNames>(event: E, ...args: Parameters<VapiEventListeners[E]>): boolean;
    removeListener<E extends VapiEventNames>(event: E, listener: VapiEventListeners[E]): this;
    removeAllListeners(event?: VapiEventNames): this;
}
export default class Vapi extends VapiEventEmitter {
    private started;
    private call;
    private speakingTimeout;
    private averageSpeechLevel;
    constructor(apiToken: string, apiBaseUrl?: string);
    private cleanup;
    start(assistant: CreateAssistantDTO | string, assistantOverrides?: OverrideAssistantDTO): Promise<Call | null>;
    private onAppMessage;
    private handleRemoteParticipantsAudioLevel;
    stop(): void;
    send(message: VapiClientToServerMessage): void;
    setMuted(mute: boolean): void;
    isMuted(): boolean;
}
export {};
