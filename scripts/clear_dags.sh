#!/bin/bash

# ;set -e

SUMMARIZATION_DAGS=(
    "X3MInstanceSummarization"
)
    # "X3MWaterfallsSummarization"
    # "X3MAppsSummarization"
    # "X3M_DAU"
ENV="prd" # "stg"
BASE_DAG_RUN_CLEAR_CMD="python airflow-cli.py --env $ENV dag-runs clear"

for dag_id in ${SUMMARIZATION_DAGS[@]}; do
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T00:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T01:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T02:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T03:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T04:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T05:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T06:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T07:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T08:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T09:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T10:00:00+00:00
   $BASE_DAG_RUN_CLEAR_CMD $dag_id scheduled__2023-02-09T11:00:00+00:00
done
