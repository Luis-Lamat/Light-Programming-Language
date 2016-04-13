echo "\n[$(date)] =========================================== " > latest_log.txt
python light_parser.py 'test/'$1 2>&1 | tee -a latest_log.txt
