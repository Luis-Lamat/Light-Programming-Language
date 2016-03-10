echo "\n[$(date)] =========================================== " >> latest_log.txt
python light_parser.py input.in  2>&1 | tee -a latest_log.txt
