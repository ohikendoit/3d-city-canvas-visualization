# Get this figure: fig = py.get_figure("https://plotly.com/~yaera/17/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~yaera/17/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Kosovo PS x Economy", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plotly.com/~yaera/17/").get_data()[0]["y"]

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "meta": {"columnNames": {
      "x": "Decision-making", 
      "y": "SocioEconEnv", 
      "z": "Interactions", 
      "text": "F", 
      "marker": {
        "size": "E", 
        "color": "Values-color"
      }
    }}, 
  "mode": "markers", 
  "type": "scatter3d", 
  "x": ["0.77", "1.8", "1.7", "2.5", "0.77", "1.6", "6.8", "6.8", "7.7", "7.8", "6.55", "7.15", "7.15", "7", "7.6", "7", "7.6", "6.25", "6.5", "6.6", "7.15", "7.55", "7.7", "7.75", "7.8", "7.85", "6.85", "7.1", "7.4", "6.55", "1.6", "6.65", "6.65", "6.7", "6.7", "7.2", "3", "7.35", "3", "7.35", "6.75", "6.65", "7.35", "6.9", "7.3", "6.65", "6.95", "6.75", "6.7", "6.75", "6.8", "6.95", "6.7", "6.8", "7.2", "7.25", "1.6", "1.6", "3.3", "6.35", "6.45", "6.2", "1.6", "3.2", "6.3", "1.4", "6.3", "6.4", "7.45", "7.5", "7.65", "0.6", "0.7", "0.8", "0.9", "1", "1.2", "1.3", "1.5", "0.3", "0.4", "0.5", "1.59", "2.4", "2.6", "7.05", "1.1", "3.1"], 
  "y": ["1.3", "9.2", "9.3", "8.5", "8.6", "8.7", "8.8", "8.9", "9", "9.1", "0.55", "6.3", "6.35", "6.4", "6.45", "6.5", "6.55", "6.6", "6.65", "6.7", "6.75", "6.8", "6.85", "6.9", "6.95", "7", "7.05", "7.1", "7.15", "7.2", "7.25", "7.3", "7.35", "7.4", "7.45", "7.5", "4.3", "4.35", "4.4", "4.45", "4.5", "4.55", "4.6", "4.65", "4.7", "4.75", "4.8", "4.85", "4.9", "4.95", "5", "5.05", "5.1", "5.15", "5.2", "5.25", "5.3", "0.4", "2.6", "2.8", "3", "3.2", "3.4", "0.25", "0.3", "0.35", "0.45", "0.5", "0.6", "0.65", "0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "1", "1.05", "1.1", "1.15", "1.2", "1.25", "1.35", "1.4", "1.45", "1.5", "1.55", "1.6"], 
  "z": ["3.8", "2.25", "3.2", "2.38", "3.8", "2.2", "0.8", "3.88", "3", "3.1", "2.6", "5.1", "6.7", "1", "1.7", "4.6", "4.8", "2.3", "2.55", "2.65", "2.75", "2.9", "3", "3.05", "3.1", "3.15", "0.9", "1.2", "1.6", "2.6", "2.2", "0.5", "4.5", "0.6", "3.56", "1.3", "4.4", "4.7", "7", "7.2", "3.29", "0.5", "1.5", "4.2", "4.3", "4.5", "5", "5.2", "0.6", "0.7", "0.8", "2.7", "3.56", "3.88", "1.3", "1.4", "2.2", "2.2", "2.1", "2.4", "2.5", "", "2.2", "9", "4.9", "2.15", "2.35", "2.45", "2.8", "2.85", "2.95", "3.25", "3.3", "3.35", "3.4", "3.45", "3.5", "3.55", "3.6", "3.65", "3.7", "3.75", "3.85", "3.9", "2.89", "1.1", "1.8", "1.9"], 
  "marker": {
    "meta": {"columnNames": {
        "size": "E", 
        "color": "Values-color"
      }}, 
    "sizemin": 22, 
    "size": ["10", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 
    "colorbar": {"title": {"text": "z"}}, 
    "color": ["3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "1", "3", "1", "3", "1", "3", "3", "3", "3", "3", "3", "3", "3", "3", "1", "3", "3", "3", "3", "3", "3", "3", "3", "1", "3", "1", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "1", "3", "3", "1", "3", "1", "1", "3", "1", "3", "1", "3", "1", "3", "1", "1", "1", "1", "1", "1", "3", "1", "1", "1", "3", "1", "3", "1", "1", "3"], 
    "showscale": False, 
    "colorscale": [
      [0, "#a50026"], [0.1, "#d73027"], [0.2, "#f46d43"], [0.3, "#fdae61"], [0.4, "#fee08b"], [0.5, "#ffffbf"], [0.6, "#d9ef8b"], [0.7, "#a6d96a"], [0.8, "#66bd63"], [0.9, "#1a9850"], [1, "#006837]
  }, 
  "text": ["• (WB)
  Sustainability checklist for fiscal stimulus packages", "• (UNDP) Support government in integrating greener measures into
  economic policy, including promoting the use of renewable energy", "• (UNDP) Policy advice and dialogue for Kosovo institutions to
  build back towards a healthier environment and lower-carbon economy", "• (UNDP) Policy advice and dialogue for Kosovo institutions to
  build back towards a healthier environment and lower-carbon economy", "• (WB) Sustainability checklist for fiscal stimulus packages", "• (UNDP) Develop and support early recovery measures to respond
  to negative socio-economic impacts by COVID-19", "• (UNDP) Support creation of green jobs as an integral part of
  economic transformation", "• (UNDP) Support creation of green jobs as an integral part of
  economic transformation", "• (UNDP) Support green recovery through transitioning to
  macroeconomic models of low carbon development", "• (UNDP) Support government to include environmentally
  appropriate stimulus measures for bailout packages for COVID-19, including
  promotion of renewable energy", "• (UN Women) Support key institutions to make informed budgetary
  allocation towards gender equality, in line with national and international
  commitments, and support local government to apply Gender Responsive
  Budgeting tools in their plans and budgets", "• (UNDP) Promote crowdfunding academy as means of mobilising
  alternative finance for sustainable recovery", "• (UNDP) Promote crowdfunding academy as means of mobilising
  alternative finance for sustainable recovery", "• (UNDP) Support incubator events for young innovators to find
  solutions to the COVID-19 crisis", "• (FAO) Provide capacity-building support to smallholder
  farmers, with focus on women, youth, producers’ associations and cooperatives", "• (UNDP) Support incubator events for young innovators to find
  solutions to the COVID-19 crisis", "• (FAO) Provide capacity-building support to smallholder
  farmers, with focus on women, youth, producers’ associations and cooperatives", "• (UNDP/UNV) Support the Public Employment Agency (and
  ultimately Kosovo job seekers) through provision of PPEs, technical and human
  resource capacity and in operationalising their online application system", "• (UN Women) Capacity development support to Ministry of Finance
  to conduct gender analysis of the impact of COVID-19, develop guidelines and
  decide on sector specific emergency response", "• (UN Women) Support key institutions in the integration of
  unpaid care work in national statistics and data analysis", "• (UNDP) Promote crowdfunding academy as means of mobilising
  alternative finance for sustainable recovery", "• (FAO) Support improved forest-based value chains through
  financial and capacity-building support", "• (UNDP) Support green recovery through transitioning to
  macroeconomic models of low carbon development", "• (UNDP) Support fiscal institutions in monitoring the
  resilience of fiscal stimulus and its impact on the poor, women and
  vulnerable groups", "• (UNDP) Support government to include environmentally
  appropriate stimulus measures for bailout packages for COVID-19, including
  promotion of renewable energy", "• (WB) Potential economic recovery development policy loan in
  consultation with the government in support of implementing some of the
  policies needed for economic recovery", "• (UNHCR) Support provision of vocational training and prepare
  vulnerable refugees, returnees and IDPs for the labour market", "• (UNICEF) Support online skills building programmes UPSHIFT,
  PONDER and PODIUM", "• (WB) Empower younger youth (ages 15-20) to build skills
  through social entrepreneurship and civic engagement activities", "• (UN Women) Support key institutions to make informed budgetary
  allocation towards gender equality, in line with national and international
  commitments, and support local government to apply Gender Responsive
  Budgeting tools in their plans and budgets", "• (UNDP) Develop and support early recovery measures to respond
  to negative socio-economic impacts by COVID-19", "• Support income generating activities for vulnerable persons,
  including through establishment of MSMEs for non-majority community members,
  returnees and IDPs (IOM), diaspora engagement through knowledge, skills and
  funds transfer (IOM), and support to SMEs to recover their business and
  create new jobs for registered job seekers (UNDP)", "• Support income generating activities for vulnerable persons,
  including through establishment of MSMEs for non-majority community members,
  returnees and IDPs (IOM), diaspora engagement through knowledge, skills and
  funds transfer (IOM), and support to SMEs to recover their business and
  create new jobs for registered job seekers (UNDP)", "• (IOM) Support establishment of regularised labour migration,
  including improved skills-to-jobs matching, protection of migrant workers,
  facilitation of seasonal and more permanent foreign employment opportunities", "• (IOM) Support establishment of regularised labour migration,
  including improved skills-to-jobs matching, protection of migrant workers,
  facilitation of seasonal and more permanent foreign employment opportunities", "• (UNHCR) Support women's economic empowerment and
  socio-economic inclusion", "• (UNDP) Support active engagement of CSOs and the private
  sector, including business networks and SMEs, in the response to COVID-19", "• (UN Women) Support women entrepreneurs, women from DV shelters
  and organisations working with conflict-related sexual violence in producing
  prevention supplies/PPE and to market women-produced items", "• (UNDP) Support active engagement of CSOs and the private
  sector, including business networks and SMEs, in the response to COVID-19", "• (UN Women) Support women entrepreneurs, women from DV shelters
  and organisations working with conflict-related sexual violence in producing
  prevention supplies/PPE and to market women-produced items", "• (UNDP) Continue active labour market measures in cooperation
  with the Public Employment Agency with a focus on women economic empowerment", "• Support income generating activities for vulnerable persons,
  including through establishment of MSMEs for non-majority community members,
  returnees and IDPs (IOM), diaspora engagement through knowledge, skills and
  funds transfer (IOM), and support to SMEs to recover their business and
  create new jobs for registered job seekers (UNDP)", "• (UN Women) Support women entrepreneurs, women from DV shelters
  and organisations working with conflict-related sexual violence in producing
  prevention supplies/PPE and to market women-produced items", "• (WB) Provide grants to SMEs to deal with the impact of the
  COVID crisis and to increase their export capacities", "• (UN Women) Provide small grants for women-owned SMEs and
  start-up businesses", "• Support income generating activities for vulnerable persons,
  including through establishment of MSMEs for non-majority community members,
  returnees and IDPs (IOM), diaspora engagement through knowledge, skills and
  funds transfer (IOM), and support to SMEs to recover their business and
  create new jobs for registered job seekers (UNDP)", "• (WB) Capitalise the Kosovo Credit Guarantee Fund to help SMEs
  in getting access to finance through financial institutions", "• (UNDP) Continue active labour market measures in cooperation
  with the Public Employment Agency with a focus on women economic empowerment", "• (IOM) Support establishment of regularised labour migration,
  including improved skills-to-jobs matching, protection of migrant workers,
  facilitation of seasonal and more permanent foreign employment opportunities", "• (UNDP) Continue active labour market measures in cooperation
  with the Public Employment Agency with a focus on women economic empowerment", "• (UNDP) Support creation of green jobs as an integral part of
  economic transformation", "• (WB) Capitalise the Kosovo Credit Guarantee Fund to help SMEs
  in getting access to finance through financial institutions", "• (IOM) Support establishment of regularised labour migration,
  including improved skills-to-jobs matching, protection of migrant workers,
  facilitation of seasonal and more permanent foreign employment opportunities", "• (UNDP) Support creation of green jobs as an integral part of
  economic transformation", "• (UNHCR) Support women's economic empowerment and
  socio-economic inclusion", "• (UNICEF) Support Kosovo Generation Unlimited matching platform
  for paid internships", "• (UNDP) Develop and support early recovery measures to respond
  to negative socio-economic impacts by COVID-19", "• (UNDP) Develop and support early recovery measures to respond
  to negative socio-economic impacts by COVID-19", "• (WB) Emergency COVID 19 project (US$50m) supporting the health
  sector and implementation of the fiscal response package, specifically some
  measures related to social protection, to help mitigate the fiscal impact of
  the COVID crisis, such as the reduction in tax revenue", "• (ILO) Support institutions in preventing child labour as a
  result of COVID", "• (UNFPA) Support integration of gender-responsive family
  policies at central level and in the workplace", "• (UN-Habitat) Strategic gender frameworks for north
  municipalities, with focus on issues amplified by the impact of the pandemic
  (mobility, safety, economic empowerment)", "• (UNDP) Develop and support early recovery measures to respond
  to negative socio-economic impacts by COVID-19", "• Joint global Call to Action “Remittances in Crisis – How to
  Keep them Flowing,” which draws the attention of the international community
  to socio-economic effects of COVID on remittances and proposes a set of
  concrete measures. (Member state initiative supported by IOM, UNDP, WB)", "• (ILO) Support tri and bi partite negotiations on measures for
  coping with the COVID-19 outbreak", "• Support institutions to develop and implement
  gender-responsive Occupational Safety and Health policies (ILO, UNOPS, UN
  Women)", "• (ILO) Support tri and bi partite negotiations on measures for
  coping with the COVID-19 outbreak", "• (UNDP) Support institutions in strategic planning of recovery
  efforts across inter-sectoral priorities", "• (FAO) Development of a surveillance system to capture effects
  of COVID19 on agricultural production, livelihoods and food supply chain", "• (FAO) Ensure continuity in the functioning of domestic food
  supply chain", "• (UNODC) Prevention of Corruption in the allocation and
  distribution of COVID-19 economic rescue packages", "• (UNDP) Support informed policy dialogue and future programming
  through continuous impact assessment, jointly with other partners", "• (FAO) Rapid survey of food supply chains in Europe (including
  Kosovo)", "• (ILO) Assessment of short- and medium-term effects of the
  outbreak on employment and labour market and survey on impact on enterprise", "• (IOM) Rapid assessment of needs of previously supported
  businesses owned by non-majority", "• (UNDP, UNFPA, UN Women) Rapid socio-economic impact assessment
  on households and businesses", "• (UNHCR) COVID-19 needs assessments, analysis and
  registration/data management for asylum seekers, refugees, voluntary minority
  returnees and IDPs", "• (WB) COVID-19 Impact Assessment on Western Balkans (Labour
  Markets)", "• (ILO) Advice on labour legislation to cover unprotected,
  non-standard workers (seasonal, self-employed, or digital platform workers)", "• (WB) Assessment of Social Protection Responses to COVID-19 in
  the Western Balkans", "• (WB) Assessment of Western Balkans Labour Markets under the
  COVID19 Shock", "• (WB) World Bank, Western Balkans Regular Economic Report No.
  17, Spring 2020 (Kosovo background note).", "• (WB) World Bank, Western Balkans Regular Economic Report No.
  18, (planned for Fall 2020).", "• (UNICEF) Collect data on COVID-19 effect on children and women
  and regular engagement with adolescents and youth through U-Report platform", "• (UNDP) Support informed policy dialogue and future programming
  through continuous impact assessment, jointly with other partners", "• (UNDP) Promote crowdfunding and other ways of mobilising
  alternative finance for addressing the needs arising from COVID-19", "• (UNICEF) Collect data on COVID-19 effect on children and women
  and regular engagement with adolescents and youth through U-Report platform", "• (UN Women) Promote strategies for women's economic empowerment
  and recovery, including decent work, safe and healthy work environments, with
  a focus on women from the most vulnerable communities"], 
  "hoverinfo": "text", 
  "hoverlabel": {"align": "auto"}, 
  "hovertemplate": "", 
  "autocolorscale": False
}
data = Data([trace1])
layout = {
  "font": {"family": "Overpass"}, 
  "scene": {
    "xaxis": {
      "type": "linear", 
      "dtick": 2, 
      "range": [0, 8], 
      "title": {"text": "Decision-Making"}, 
      "showline": False, 
      "tickmode": "linear", 
      "autorange": False, 
      "showspikes": True, 
      "showticklabels": False
    }, 
    "yaxis": {
      "type": "linear", 
      "dtick": 2, 
      "range": [0, 10], 
      "title": {"text": "Socio-Economic Environment"}, 
      "showgrid": True, 
      "showline": True, 
      "tickmode": "linear", 
      "autorange": False, 
      "showticklabels": False
    }, 
    "zaxis": {
      "type": "linear", 
      "dtick": 2, 
      "range": [0, 10], 
      "title": {"text": "Interactions"}, 
      "tickmode": "linear", 
      "autorange": False, 
      "showticklabels": False
    }, 
    "camera": {
      "up": {
        "x": 0, 
        "y": 0, 
        "z": 1
      }, 
      "eye": {
        "x": 1.4690252763787919, 
        "y": -1.5548243882241175, 
        "z": 0.33464288300174966
      }, 
      "center": {
        "x": 0, 
        "y": 0, 
        "z": 0
      }, 
      "projection": {"type": "perspective"}
    }, 
    "aspectmode": "auto", 
    "aspectratio": {
      "x": 0.904917109163023, 
      "y": 1.0847019652881271, 
      "z": 1.018780851375589
    }
  }, 
  "title": {"text": "PS on UN Kosovo Socio-Economic Response (Economy)"}, 
  "autosize": True, 
  "colorway": ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#666666"], 
  "template": {
    "data": {
      "bar": [
        {
          "type": "bar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "table": [
        {
          "type": "table", 
          "cells": {
            "fill": {"color": "#EBF0F8"}, 
            "line": {"color": "white"}
          }, 
          "header": {
            "fill": {"color": "#C8D4E3"}, 
            "line": {"color": "white"}
          }
        }
      ], 
      "carpet": [
        {
          "type": "carpet", 
          "aaxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }, 
          "baxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }
        }
      ], 
      "mesh3d": [
        {
          "type": "mesh3d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "contour": [
        {
          "type": "contour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "heatmap": [
        {
          "type": "heatmap", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatter": [
        {
          "type": "scatter", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "surface": [
        {
          "type": "surface", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "heatmapgl": [
        {
          "type": "heatmapgl", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "histogram": [
        {
          "type": "histogram", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "parcoords": [
        {
          "line": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}, 
          "type": "parcoords"
        }
      ], 
      "scatter3d": [
        {
          "type": "scatter3d", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattergl": [
        {
          "type": "scattergl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "choropleth": [
        {
          "type": "choropleth", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattergeo": [
        {
          "type": "scattergeo", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2d": [
        {
          "type": "histogram2d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatterpolar": [
        {
          "type": "scatterpolar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "contourcarpet": [
        {
          "type": "contourcarpet", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattercarpet": [
        {
          "type": "scattercarpet", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattermapbox": [
        {
          "type": "scattermapbox", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterpolargl": [
        {
          "type": "scatterpolargl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterternary": [
        {
          "type": "scatterternary", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2dcontour": [
        {
          "type": "histogram2dcontour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ]
    }, 
    "layout": {
      "geo": {
        "bgcolor": "white", 
        "showland": True, 
        "lakecolor": "white", 
        "landcolor": "white", 
        "showlakes": True, 
        "subunitcolor": "#C8D4E3"
      }, 
      "font": {"color": "#2a3f5f"}, 
      "polar": {
        "bgcolor": "white", 
        "radialaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }, 
        "angularaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }
      }, 
      "scene": {
        "xaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "yaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "zaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }
      }, 
      "title": {"x": 0.05}, 
      "xaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "yaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "ternary": {
        "aaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "baxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "caxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "bgcolor": "white"
      }, 
      "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#19d3f3", "#e763fa", "#fecb52", "#ffa15a", "#ff6692", "#b6e880"], 
      "hovermode": "closest", 
      "colorscale": {
        "diverging": [
          [0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419], 
        "sequential": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe], 
        "sequentialminus": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe]
      }, 
      "plot_bgcolor": "white", 
      "paper_bgcolor": "white", 
      "shapedefaults": {
        "line": {"width": 0}, 
        "opacity": 0.4, 
        "fillcolor": "#506784"
      }, 
      "annotationdefaults": {
        "arrowhead": 0, 
        "arrowcolor": "#506784", 
        "arrowwidth": 1
      }
    }, 
    "themeRef": "PLOTLY_WHITE"
  }, 
  "colorscale": {"sequential": [
      [0, "#0508b8"], [0.08333333333333333, "#1910d8"], [0.16666666666666666, "#3c19f0"], [0.25, "#6b1cfb"], [0.3333333333333333, "#981cfd"], [0.4166666666666667, "#bf1cfd"], [0.5, "#dd2bfd"], [0.5833333333333334, "#f246fe"], [0.6666666666666666, "#fc67fd"], [0.75, "#fe88fc"], [0.8333333333333334, "#fea5fd"], [0.9166666666666666, "#febefe"], [1, "#fec3fe]}, 
  "hoverlabel": {"align": "auto"}, 
  "showlegend": False
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)