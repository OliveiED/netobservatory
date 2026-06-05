--
-- PostgreSQL database dump
--

\restrict C20QWRRRBRWflXs3JsZbBq8bJe0pLi9zldbXiArpFcX63D504F8wiKTDQZKIszE

-- Dumped from database version 15.18 (Debian 15.18-0+deb12u1)
-- Dumped by pg_dump version 15.18 (Debian 15.18-0+deb12u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: netobservatory
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO netobservatory;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dns_queries; Type: TABLE; Schema: public; Owner: netobservatory
--

CREATE TABLE public.dns_queries (
    id integer NOT NULL,
    "timestamp" timestamp without time zone,
    src_ip character varying(64),
    dst_ip character varying(64),
    domain text,
    query_type character varying(16),
    response_code character varying(16),
    resolved_ip character varying(64),
    ttl integer,
    latency_ms double precision,
    packet_size integer,
    country character varying(64),
    city character varying(128),
    asn integer,
    as_org text
);


ALTER TABLE public.dns_queries OWNER TO netobservatory;

--
-- Name: dns_queries_id_seq; Type: SEQUENCE; Schema: public; Owner: netobservatory
--

CREATE SEQUENCE public.dns_queries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dns_queries_id_seq OWNER TO netobservatory;

--
-- Name: dns_queries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: netobservatory
--

ALTER SEQUENCE public.dns_queries_id_seq OWNED BY public.dns_queries.id;


--
-- Name: dns_stats_hourly; Type: TABLE; Schema: public; Owner: netobservatory
--

CREATE TABLE public.dns_stats_hourly (
    id integer NOT NULL,
    timestamp_hour timestamp without time zone,
    domain text,
    query_type character varying(16),
    total_queries integer,
    avg_latency double precision,
    nxdomain_count integer
);


ALTER TABLE public.dns_stats_hourly OWNER TO netobservatory;

--
-- Name: dns_stats_hourly_id_seq; Type: SEQUENCE; Schema: public; Owner: netobservatory
--

CREATE SEQUENCE public.dns_stats_hourly_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dns_stats_hourly_id_seq OWNER TO netobservatory;

--
-- Name: dns_stats_hourly_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: netobservatory
--

ALTER SEQUENCE public.dns_stats_hourly_id_seq OWNED BY public.dns_stats_hourly.id;


--
-- Name: dns_threats; Type: TABLE; Schema: public; Owner: netobservatory
--

CREATE TABLE public.dns_threats (
    id integer NOT NULL,
    "timestamp" timestamp without time zone,
    src_ip character varying(64),
    domain text,
    threat_type character varying(64),
    risk_level character varying(32),
    description text
);


ALTER TABLE public.dns_threats OWNER TO netobservatory;

--
-- Name: dns_threats_id_seq; Type: SEQUENCE; Schema: public; Owner: netobservatory
--

CREATE SEQUENCE public.dns_threats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dns_threats_id_seq OWNER TO netobservatory;

--
-- Name: dns_threats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: netobservatory
--

ALTER SEQUENCE public.dns_threats_id_seq OWNED BY public.dns_threats.id;


--
-- Name: dns_queries id; Type: DEFAULT; Schema: public; Owner: netobservatory
--

ALTER TABLE ONLY public.dns_queries ALTER COLUMN id SET DEFAULT nextval('public.dns_queries_id_seq'::regclass);


--
-- Name: dns_stats_hourly id; Type: DEFAULT; Schema: public; Owner: netobservatory
--

ALTER TABLE ONLY public.dns_stats_hourly ALTER COLUMN id SET DEFAULT nextval('public.dns_stats_hourly_id_seq'::regclass);


--
-- Name: dns_threats id; Type: DEFAULT; Schema: public; Owner: netobservatory
--

ALTER TABLE ONLY public.dns_threats ALTER COLUMN id SET DEFAULT nextval('public.dns_threats_id_seq'::regclass);


--
-- Name: dns_queries dns_queries_pkey; Type: CONSTRAINT; Schema: public; Owner: netobservatory
--

ALTER TABLE ONLY public.dns_queries
    ADD CONSTRAINT dns_queries_pkey PRIMARY KEY (id);


--
-- Name: dns_stats_hourly dns_stats_hourly_pkey; Type: CONSTRAINT; Schema: public; Owner: netobservatory
--

ALTER TABLE ONLY public.dns_stats_hourly
    ADD CONSTRAINT dns_stats_hourly_pkey PRIMARY KEY (id);


--
-- Name: dns_threats dns_threats_pkey; Type: CONSTRAINT; Schema: public; Owner: netobservatory
--

ALTER TABLE ONLY public.dns_threats
    ADD CONSTRAINT dns_threats_pkey PRIMARY KEY (id);


--
-- Name: idx_dns_stats_hourly; Type: INDEX; Schema: public; Owner: netobservatory
--

CREATE INDEX idx_dns_stats_hourly ON public.dns_stats_hourly USING btree (timestamp_hour);


--
-- Name: idx_dns_timestamp; Type: INDEX; Schema: public; Owner: netobservatory
--

CREATE INDEX idx_dns_timestamp ON public.dns_queries USING btree ("timestamp");


--
-- PostgreSQL database dump complete
--

\unrestrict C20QWRRRBRWflXs3JsZbBq8bJe0pLi9zldbXiArpFcX63D504F8wiKTDQZKIszE

