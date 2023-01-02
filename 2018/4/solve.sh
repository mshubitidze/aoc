sort in.txt | awk -v FS="[\]:# ]" '/Guard/{g=$7}
                                    /falls/{s=$3}
                                    /wakes/{for(t=s;t<$3;++t){
                                              ++zg[g];++zgt[g","t]
                                           }
                                    }
                                    END{for(g in zg)
                                          if(zg[g]>zg[og])
                                            og=g;
                                        for(t=0;t<60;++t)
                                          if(zgt[og","t]>zgt[og","ot])
                                            ot=t;
                                        print og*ot
                                    }'

sort in.txt | awk -v FS="[\]:# ]" '/Guard/{g=$7}
                                    /falls/{s=$3}
                                    /wakes/{for(t=s;t<$3;++t)
                                              ++zgt[g","t]
                                    }
                                    END{for(gt in zgt)
                                          if(zgt[gt]>zgt[ogt])
                                            ogt=gt;
                                        split(ogt,oa,",");
                                        print oa[1]*oa[2]
                                    }'

