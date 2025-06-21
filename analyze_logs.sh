#!/bin/bash

LOG_FILE="access.log"

total=$(wc -l < "$LOG_FILE")

unique=$(awk '{print $1}' "$LOG_FILE" | sort -u | wc -l)

method_counts=$(awk '{print $6}' "$LOG_FILE" | sort | uniq -c | sort -nr)

popular_url=$(awk '{print $7}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 1)

{
    echo "Отчет о логе веб-сервера"
    echo "========================"
    echo "Общее количество запросов:     $total"
    echo "Количество уникальных IP-адресов:      $unique"
    echo ""
    echo "Количество запросов по методам:"
    echo "$method_counts"
    echo ""
    echo "Самый популярный URL: $popular_url"
} > report.txt

echo "Отчет сохранен в файл report.txt"