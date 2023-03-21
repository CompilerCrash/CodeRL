#
# Copyright (c) 2022, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#

# Reads:
# ${test_path}/????/question.txt
# Optionally reads:
# ${test_path}/????/{starter_code.py, input_output.json}
# Conditionally reads (depending on --gt_solutions):
# ${test_path}/????/{solutions.json, gen_solutions.json}
# Conditionally writes (depending on --gt_solutions):
# ${test_path}/????/{solutions_critic_scores.pkl, gen_solutions_critic_scores.pkl}

critic_path=models/codet5_finetuned_critic_binary/
tokenizer_path=models/codet5_tokenizer/
test_path=data/APPS/train/

start=0
end=1

output_path=$test_path # variable is only set to avoid an error; critic scores are always saved next to the input data

CUDA_VISIBLE_DEVICES=0 python generate.py \
  --model_path $critic_path \
  --tokenizer_path $tokenizer_path \
  --test_path $test_path \
  --output_path $output_path \
  -s $start -e $end \
  --critic_scores --gt_solutions --binary_prediction
