def Report_Generator(Final_List):
    if Final_List == []:
        return "There is no candidate protein"
    else:
        FL = sorted(Final_List, key=lambda item: item['mw'], reverse=True)
        report_lines = []
        report_lines.append("======= BioForge Analysis Report =======")
        report_lines.append("ID     Length  MW(kDa)   Strand")
        report_lines.append("-" * 52)
        for i in FL:
            ID = i["protein_id"]
            Length = i["length"]
            MW = i["mw"]
            Strand = i["strand"]
            report_lines.append(f"{ID:<9} {Length:<5} {round(int(MW)/1000, 2):<8} {Strand}")
        report = "\n".join(report_lines)
        return report