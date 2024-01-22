## Задание 1 

![!\[Alt text\](<img/!\[Alt text\](<img/1.png>)>)](<img/1.png>)

## Задание 2

![!\[Alt text\](<img/!\[Alt text\](<img/2.png>)>)](<img/2.png>)

- 100 - (avg by (instance)(irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

- node_load1 / node_load5 / node_load15

- 100 * ((avg_over_time(node_memory_MemFree_bytes[5m]) + avg_over_time(node_memory_Cached_bytes[5m]) + avg_over_time(node_memory_Buffers_bytes[5m])) / avg_over_time(node_memory_MemTotal_bytes[5m]))

- node_filesystem_avail_bytes {fstype=~"ext4|xfs"} 

## Задание 3

![!\[Alt text\](<img/!\[Alt text\](<img/3.png>)>)](<img/3.png>)

![!\[Alt text\](<img/!\[Alt text\](<img/3.1.png>)>)](<img/3.1.png>)

#### со временем на графиках не понятно почему ерунда такая - контейнеры запущены были все время

## Задание 4

[test-template.json](test-template.json) 