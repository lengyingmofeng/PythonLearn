import demjson

txt = r'''
{
    list_type: c,
    info: {
        property: {
            id: "6063502189",
            house_id: yL,
            status: c,
            isauction: "{\"entity_id\":\"2259467035122703\",\"tid\":\"-\",\"auction\":\"201\",\"soj_info\":{\"entry_source\":\"Anjuke_Hp_View\",\"from_id\":\"1\",\"project_id\":\"201\",\"source_type\":1,\"hp_type\":\"1\",\"ax_type\":\"1000010\",\"search_type\":\"filter\",\"vpid\":\"6063502189\",\"v\":\"2.0\",\"hp_page\":\"Anjuke_Hp_View\",\"channel\":\"1\",\"community_id\":\"100385662\",\"area_id\":\"3472\",\"esf_id\":6063502189,\"isauction\":201,\"pos\":0,\"trading_area_ids\":0,\"found\":0,\"prop_expire\":0,\"entry\":0,\"tradeType\":\"1\"}}",
            source_type: c,
            title: "江河双水湾 4室2厅 满五 电梯房 朝南 楼层好 随时看房",
            city_id: i,
            community_id: yM,
            broker_ids: [jZ],
            default_photo: "https:\u002F\u002Fpic1.ajkimg.com\u002Fdisplay\u002Fajk\u002Fcd80201825c13c8c0804f691c918af1f\u002F640x420c.jpg?t=5",
            no_sign_photo: "https:\u002F\u002Fpic1.ajkimg.com\u002Fdisplay\u002Fajk\u002Fcd80201825c13c8c0804f691c918af1f\u002F214x156c.jpg?t=5",
            tags: [yN, V, "景观房"],
            abtest_flow_id: b,
            tw_url: "https:\u002F\u002Fm.anjuke.com\u002Fcs\u002Fsale\u002FA6063502189\u002F?isauction=201&position=0&kwtype=filter&now_time=1640142261",
            pc_url: "https:\u002F\u002Fcs.anjuke.com\u002Fprop\u002Fview\u002FA6063502189?auction=201&hpType=1&entry=102&position=0&kwtype=filter&now_time=1640142261&spread=filtersearch_p",
            attribute: {
                price: j_,
                room_num: D,
                hall_num: e,
                toilet_num: e,
                avg_price: "11438",
                area_num: "126.8",
                house_age: aq,
                orient: bk,
                fitment_name: aR,
                floor: b,
                total_floor: ar,
                floor_level: ax,
                use_type: u,
                use_type_enum: b,
                over_tax_year: e,
                unique_prop: a,
                heating: a,
                commission_coupon_amount: a,
                role_explain: b,
                panoram_fitment: a,
                has_lift: a
            },
            flag: {
                has_video: a,
                is_guarantee: c,
                pano_url: "https:\u002F\u002Fwww.anjuke.com\u002Fpc\u002Fesf\u002Fvrview\u002F?token=AHeAlnLZ2EVtC90xIUQ6to0l%2B5h691cwwwVJq7x7oSCbSYSwQvI0epafEXmf%2FE5uDoXUe9rpDoAQNgMt1ZyCGa3EiuV7tlRJi10gmfyTWp4R4J2ucm8MGSjHFHApllOy&app_id=10002&sv=5.0&ab=1&prop_id=6063502189",
                is_landlord_listed: a,
                is_dual_core: a,
                is_auction_icon: a,
                is_xinfang: a,
                is_collect: a,
                induction_tags: [c],
                is_tfj: a,
                pano_url_action: b,
                pano_id: "49831528",
                pano_type: Q,
                is_vr_take_look: c,
                is_business_sku: a,
                is_black_golden: a,
                is_induction: c,
                vr_take_look_url: "https:\u002F\u002Fwww.anjuke.com\u002Fpanorama?p=lhhf5ciq9sf8j7cl&type=102",
                is_excellent_house: a,
                auction: a,
                top: a,
                is_government: c,
                is_full_verification: c,
                is_agency_aifang: a
            },
            post_date: "1637289350",
            commission_type: c,
            has_lift: c,
            entry: a,
            attr_tags: {
                is_landlord_listed: a,
                over_tax_year: e,
                unique_prop: a,
                has_lift: c,
                heating: a
            },
            panorama_tags: [],
            activity_icon: b,
            jump_action: b,
            house_tag: {
                name: w,
                image: x,
                dark_image: b,
                desc_title: b,
                desc_sub_title: b,
                height: j,
                width: y,
                desc: b
            },
            enable_multi_cover: a,
            cover_image_list: [],
            other_house_tag: [{
                name: J,
                image: K,
                dark_image: b,
                desc_title: b,
                desc_sub_title: b,
                height: j,
                width: L,
                desc: b
            }]
        },
        community: {
            id: yO,
            city_id: i,
            name: yP,
            address: yQ,
            default_photo: yR,
            lat: yS,
            lng: yT,
            area_id: bJ,
            area_name: bq,
            block_id: yU,
            block_name: bs,
            distance: b,
            build_type_str: bO,
            ship_type_str: v,
            flag: {
                closeSubway: c,
                closeSchool: c,
                hasPanoPhoto: c,
                hasEvaluation: a
            },
            completion_time: bB,
            tags: [bg, M, H],
            shangquan: [{
                id: cc,
                name: bs
            }],
            show_shangquan: c,
            score: cU,
            shangquan_id: cc,
            shangquan_name: bs,
            gLat: yV,
            gLng: yW
        },
        broker: {
            broker_id: jZ,
            user_id: a,
            city_id: z,
            chat_id: jZ,
            chat_user_source: A,
            name: "刘晓娇",
            photo: "https:\u002F\u002Fspic1.ajkimg.com\u002FZaosucBM3Tp5FnMFX-7VdQBD1bfKYevnJpjHMHE5W9Y2OB2eI1ozAUnV4tYECVc6zuP2FQ0mqJ0JI5VqJpc5ADfgY4IMGFbfS_2eEQe1UCtUlRhYBq3zEM61Y3MyHq20VYbwaqKW011iYoef0kQ0FkNgncySfrIpcuXmqusyxQuZhQCzZDGMX1moeoerXMQP",
            mobile: yX,
            area_id: a,
            block_id: a,
            shangquan_id: a,
            company_id: "369254",
            company_name: yY,
            store_id: "822712",
            store_name: "长沙中讯房地产经纪有限公司总店",
            store_switch: a,
            is_verify: a,
            star_score: aW,
            company_full_name: yY,
            is_polestar: a,
            role_explain: b,
            wuba_mobile: yX,
            wuba_user_id: "47858392763919",
            is_settle_activity: c,
            service_guarantee: c
        },
        tid: B,
        entityId: yL,
        other: {
            metro_desc: b,
            school_desc: b
        }
    }
}
'''

txt = txt.replace('c', '1433').replace('yL', '1434').replace('\\', '')
q = demjson.decode(txt)

print(q)