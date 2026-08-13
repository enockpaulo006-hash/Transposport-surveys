from django.shortcuts import render
from .services.kobo_service import KoboService
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import json

def get_dashboard_stats():

    stats = KoboService.dashboard_statistics()

    return {
        "stats": stats,
        "total_responses": stats["total"],
        "male_count": stats["male"],
        "female_count": stats["female"],
        "gender_labels": json.dumps(stats["gender_labels"]),
        "gender_values": json.dumps(stats["gender_values"]),
        "transport_labels": stats["transport_labels"],
        "transport_labels_json": json.dumps(stats["transport_labels"]),
        "transport_values": json.dumps(stats["transport_values"]),
        "travel_labels": stats["travel_labels"],
        "travel_labels_json": json.dumps(stats["travel_labels"]),
        "safety_labels": stats["safety_labels"],
        "safety_labels_json": json.dumps(stats["safety_labels"]),
        "safety_values": json.dumps(stats["safety_values"]),
        "age_labels": json.dumps(stats["age_labels"]),
        "age_values": json.dumps(stats["age_values"]),
        "occupation_labels": json.dumps(stats["occupation_labels"]),
        "occupation_values": json.dumps(stats["occupation_values"]),
        "travel_labels": stats["travel_labels"],
        "travel_values": json.dumps(stats["travel_values"]),
        "harassment_labels": stats["harassment_labels"],
        "harassment_labels_json": json.dumps(stats["harassment_labels"]),
        "harassment_values": json.dumps(stats["harassment_values"]),
        "most_transport": stats["most_transport"],
        "most_transport_count": stats["most_transport_count"],
        "most_age": stats["most_age"],
        "most_age_count": stats["most_age_count"],
        "most_occupation": stats["most_occupation"],
        "most_occupation_count": stats["most_occupation_count"],
        "most_safety": stats["most_safety"],
        "most_safety_count": stats["most_safety_count"],
        "most_harassment": stats["most_harassment"],
        "most_harassment_count": stats["most_harassment_count"],
        "most_travel_time": stats["most_travel_time"],
        "most_travel_time_count": stats["most_travel_time_count"],
    }

@login_required(login_url="login")
def home(request):

    context = get_dashboard_stats()

    print(context["stats"]["most_transport"])
    print(context["stats"]["most_transport_count"])

    context["responses"] = context["stats"]["responses"]

    context["active_page"] = "dashboard"

    context["most_transport"] = context["stats"]["most_transport"]
    context["most_transport_count"] = context["stats"]["most_transport_count"]

    context["most_age"] = context["stats"]["most_age"]
    context["most_age_count"] = context["stats"]["most_age_count"]

    return render(
        request,
        "dashboard/home.html",
        context
    )
    
@login_required(login_url="login")
def responses(request):

    context = get_dashboard_stats()

    data = context["stats"]["responses"]
    search = request.GET.get("search", "")

    if search:

        filtered = []

        for row in data:

            text = str(row).lower()

            if search.lower() in text:

                filtered.append(row)

        data = filtered

    paginator = Paginator(data, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    if data:
        print(data[0])

    return render(
    request,
    "dashboard/responses.html",
    {
        "page_obj": page_obj,
        "total": len(data),
        "search": search,
        "active_page": "responses",
    },
)
    
@login_required(login_url="login")
def gender_analysis(request):

    context = get_dashboard_stats()

    context["active_page"] = "gender"

    return render(
        request,
        "dashboard/gender_analysis.html",
        context
    )
    
@login_required(login_url="login")    
def transport_analysis(request):

    context = get_dashboard_stats()
    
    context["most_transport"] = context["stats"]["most_transport"]
    context["most_transport_count"] = context["stats"]["most_transport_count"]

    context["responses"] = context["stats"]["responses"]

    context["active_page"] = "transport"

    return render(
        request,
        "dashboard/transport_analysis.html",
        context
    )  
  
@login_required(login_url="login")    
def safety_analysis(request):

    context = get_dashboard_stats()

    context["active_page"] = "safety"

    return render(
        request,
        "dashboard/safety_analysis.html",
        context
    )
    
@login_required(login_url="login")    
def reports(request):

    context = get_dashboard_stats()

    context["active_page"] = "reports"

    return render(
        request,
        "dashboard/reports.html",
        context
    )
    
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(
            request,
            "dashboard/login.html",
            {
                "error": "Invalid username or password"
            }
        )

    return render(
        request,
        "dashboard/login.html"
    )
    
def logout_view(request):

    logout(request)

    return redirect("login")

@login_required(login_url="login")
def generate_report(request):

    stats = KoboService.dashboard_statistics()

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = (
        'attachment; filename="Transport_Survey_Report.pdf"'
    )

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.fontName = "Times-Bold"
    title_style.spaceAfter = 30

    heading_style = styles["Heading2"]
    heading_style.fontName = "Times-Bold"
    heading_style.spaceAfter = 15

    normal_style = styles["Normal"]
    normal_style.fontName = "Times-Roman"
    normal_style.leading = 22
    normal_style.spaceAfter = 12

    story = []

    story.append(
        Paragraph(
            "<b>GENDER-DISAGGREGATED TRANSPORT MOBILITY SURVEY SYSTEM REPORT</b>",
            title_style
        )
    )

    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d %B %Y %H:%M')}",
            normal_style
        )
    )
    story.append(
    Paragraph(
        "<b>Executive Summary</b>",
        heading_style
     )
    )

    story.append(
    Paragraph(
        f"""
        This report presents a summary of the Gender-Disaggregated
        Transport Mobility Survey collected through KoboToolbox.
        The analysis includes transport preferences, gender distribution,
        travel behaviour, safety perception, and reported incidents.
        The statistics below are generated automatically from the latest
        survey responses.
        """,
        normal_style
     )
    )

    table_data = [

     ["Statistic", "Value"],
     ["Total Responses", stats["total"]],
     ["Male Participants", stats["male"]],
     ["Female Participants", stats["female"]],
     ["Most Used Transport", stats["most_transport"]],
     ["Responses", stats["most_transport_count"]],
     ["Most Common Travel Time", stats["most_travel_time"]],
     ["Most Common Safety Level", stats["most_safety"]],
     ["Most Reported Incident", stats["most_harassment"]],
    ]

    table = Table(
        table_data,
        colWidths=[250, 180]
    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2563eb")),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("FONTNAME", (0,0), (-1,0), "Times-Bold"),
            ("BOTTOMPADDING", (0,0), (-1,0), 10),
            ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),
            ("GRID", (0,0), (-1,-1), 1, colors.grey),
            ("FONTNAME", (0,1), (-1,-1), "Times-Roman"),
            ("ALIGN", (1,1), (-1,-1), "CENTER"),
            ("BOTTOMPADDING", (0,1), (-1,-1), 8),

        ])

    )

    story.append(table)
    story.append(
    Paragraph(
        "<br/><b>Recommendations</b>",
        heading_style
        )
    )

    story.append(
    Paragraph(
        f"""
        The most commonly used mode of transport is
        <b>{stats['most_transport']}</b>. Consider prioritizing improvements to this
        transport mode.

        <br/>

        Continue collecting transport mobility data to support evidence-based
        planning and decision making.

        <br/>

        Improve transport safety initiatives based on survey responses and
        reported incidents.
        """,
        normal_style
        )
    )
    
    doc.build(story)

    return response
