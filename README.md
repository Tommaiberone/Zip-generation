# Seq2Seq medium edit distance

| Model               | Short Sentences /Randomized <br> (avg gold len = 55.33)  | Medium Sentences <br> (avg gold len = 97.22) | Count Zero short/randomized   | Count Zero w/medium
|---------------------|----------------------------------------------|----------------------------------------------|----------------------|--------------------
| bart-base           | 7.3                                          | /                                            | /                    |
| bart-large          | 6.965  /  7.80375                            | 29.86                                        | 37 /  0              | 0
| t5                  | 11.79375                                     | /                                            | /                    |
| lstm                | 57.6128                                      | /                                            | /                    |
| Transformer         | 57.552                                       | /                                            | /                    |
| LoRA Opt-350m       | 11.79                                        | /                                            | /                    |


