#
# Copyright (c) 2022, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#

# Reads:
# ${train-path}/????/{question.txt, solutions.json, gen_solutions_critic_scores.pkl}
# Conditionally reads (depending on --relative_returns):
# ${train-path}/????/baseline_solutions.json
# Optionally reads:
# ${train-path}/????/starter_code.py
# Writes:
# ${save_dir}/args.json
# ${save_dir}/final_checkpoint/*
# ${save_dir}/*/*

# Run code in debugging mode (without deepspeed)
python \
  train.py \
  --batch-size-per-replica 1 --grad-acc-steps 4 \
  --epochs 10 --lr 2e-5 \
  --save-freq 1000 --log-freq 10 --save_total_limit 5 \
  --fp16 \
  --tuning_mode rl --model codet5-large \
  --model_path models/codet5_finetuned_codeRL/ \
  --relative_returns \
  --db
