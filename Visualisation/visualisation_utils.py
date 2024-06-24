import json
import pandas as pd 
import os



def export_fluxes_for_compressed_map(fluxes, output_file):
    flux_dict=pd.Series.to_dict(fluxes)

    #Assign a flux to each Compressed Pathway. Update this if the map is changed!-----
    cp_list={"Chorismate_Biosynthesis(CP)":flux_dict["CHORS"],
         "Histidine_biosynthesis(CP)":flux_dict["HISTD"],
         "Tryptophan_Biosynthesis(CP)":flux_dict["TRPS2"],
         "3mob_Biosynthesis(CP)":flux_dict["DHAD1"],
         "Leucine_Biosynthesis(CP)":flux_dict["LEUTAi"],
         "Lysine_Biosynthesis(CP)":flux_dict["DAPDC"],
         "Isoleucine_Biosynthesis(CP)":flux_dict["ILETA"],
         "Methionine_Biosynthesis(CP)":flux_dict["METS"],
         "H2S_Biosynthesis(CP)":flux_dict["SULR"],
         "Proline_Biosynthesis(CP)":flux_dict["P5CR"],
         "Arginine_Biosynthesis(CP)":flux_dict["ARGSL"],
         "UDP_Biosynthesis(CP)":flux_dict["UMPK"],
         "dCTP_Biosynthesis(CP)":flux_dict["NDPK7"],
         "dTTP_Biosynthesis(CP)":flux_dict["NDPK4"],
         "Aicar_Biosynthesis(CP)":flux_dict["ADSL2r"],
         "tdec2eACP_Biosynthesis(CP)":flux_dict["3HAD100"],
         "hdeACP_Biosynthesis(CP)":flux_dict["EAR161x"],
         "3hmrsACP_Biosynthesis(CP)":flux_dict["3OAR140"],
         "Palmitoyl_ACP_Biosynthesis(CP)":flux_dict["EAR160x"],
            }
    #----------------------------------------------------------------------
    flux_dict.update(cp_list)
    with open(output_file, 'w') as f:
        json.dump(flux_dict, f)



def flux2json(fluxes,filename):
    dic=pd.Series.to_dict(fluxes)
    with open(filename, 'w') as f:
        json.dump(dic, f)