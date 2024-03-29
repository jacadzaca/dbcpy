import dataclasses
from dbcpy.loc import Loc

# @see https://wowdev.wiki/DB/Spell#3.3.5.12340
_fields = {
    'entry': int,
    'spell_category': int,
    'dispell_type': int,
    'spell_mechanics': int,
    'attributes': int,
    'attributes_ex': int,
    'attributes_exb': int,
    'attributes_exc': int,
    'attributes_exd': int,
    'attributes_exe': int,
    'attributes_exf': int,
    'attributes_exg': int,
    'stances': int,
    'unknown': int,
    'excluded_stances_flag': int,
    'unknown1': int,
    'targets_flag': int,
    'target_creature_type': int,
    'spell_focus': int,
    'facing_caster_flag': int,
    'caster_aura_state': int,
    'target_aura_state': int,
    'caster_aura_state_not': int,
    'target_aura_state_not': int,
    'caster_aura_spell': int,
    'target_aura_spell': int,
    'exclude_caster_aura_spell': int,
    'exclude_target_aura_spell': int,
    'casting_time_index': int,
    'cooldown': int,
    'global_cooldown': int,
    'interrupt_flags': int,
    'aura_interrupt_flags': int,
    'channel_interupt_flags': int,
    'proc_flag': int,
    'proc_chance': int,
    'proc_charges': int,
    'max_level': int,
    'base_level': int,
    'spell_level': int,
    'duration_index': int,
    'power_type': int,
    'mana_cost': int,
    'mana_cost_per_level': int,
    'mana_cost_per_second': int,
    'mana_per_second_per_level': int,
    'range': int,
    'speed': float,
    'modal_next_spell': int,
    'stack_amount': int,
    'totem': int,
    'totem1': int,
    'reagent': int,
    'reagent1': int,
    'reagent2': int,
    'reagent3': int,
    'reagent4': int,
    'reagent5': int,
    'reagent6': int,
    'reagent7': int,
    'reagent_count': int,
    'reagent_count1': int,
    'reagent_count2': int,
    'reagent_count3': int,
    'reagent_count4': int,
    'reagent_count5': int,
    'reagent_count6': int,
    'reagent_count7': int,
    'equipped_item_class': int,
    'equipped_item_sub_class_mask': int,
    'equipped_item_class_inventory_type_mask': int,
    'effect': int,
    'effect1': int,
    'effect2': int,
    'effect_die_sides': int,
    'effect_die_sides1': int,
    'effect_die_sides2': int,
    'effect_real_points_per_level': float,
    'effect_real_points_per_level1': float,
    'effect_real_points_per_level2': float,
    'effect_base_points': int,
    'effect_base_points1': int,
    'effect_base_points2': int,
    'effect_mechanic': int,
    'effect_mechanic1': int,
    'effect_mechanic2': int,
    'effect_implicit_target': int,
    'effect_implicit_target1': int,
    'effect_implicit_target2': int,
    'effect_implicit_target3': int,
    'effect_implicit_target4': int,
    'effect_implicit_target5': int,
    'effect_radius': int,
    'effect_radius1': int,
    'effect_radius2': int,
    'effect_apply_aura_name': int,
    'effect_apply_aura_name1': int,
    'effect_apply_aura_name2': int,
    'effect_aura_period': int,
    'effect_aura_period1': int,
    'effect_aura_period2': int,
    'effect_multiple_value': int,
    'effect_multiple_value1': int,
    'effect_multiple_value2': int,
    'effect_chain_target': int,
    'effect_chain_target1': int,
    'effect_chain_target2': int,
    'effect_item_type': int,
    'effect_item_type1': int,
    'effect_item_type2': int,
    'effect_misc_value': int,
    'effect_misc_value1': int,
    'effect_misc_value2': int,
    'effect_misc_value3': int,
    'effect_misc_value4': int,
    'effect_misc_value5': int,
    'effect_trigger_spell': int,
    'effect_trigger_spell1': int,
    'effect_trigger_spell2': int,
    'effect_points_per_combo_point': float,
    'effect_points_per_combo_point1': float,
    'effect_points_per_combo_point2': float,
    'effect_spell_class_mask': int,
    'effect_spell_class_mask1': int,
    'effect_spell_class_mask2': int,
    'effect_spell_class_mask3': int,
    'effect_spell_class_mask4': int,
    'effect_spell_class_mask5': int,
    'effect_spell_class_mask6': int,
    'effect_spell_class_mask7': int,
    'effect_spell_class_mask8': int,
    'spell_visual': int,
    'spell_visual1': int,
    'icon_id': int,
    'active_icon_id': int,
    'priority': int,
    'name': Loc,
    'subname': Loc,
    'description': Loc,
    'tooltip': Loc,
    'mana_cost_percentage': int,
    'start_recovery_category': int,
    'start_recovery_time': int,
    'max_target_level': int,
    'spell_class_set': int,
    'spell_class_mask': int,
    'spell_class_mask1': int,
    'spell_class_mask2': int,
    'max_affected_targets': int,
    'defense_type': int,
    'prevention_type': int,
    'stance_bar_order': int,
    'effect_chain_amplitude': float,
    'effect_chain_amplitude1': float,
    'effect_chain_amplitude2': float,
    'min_faction_id': int,
    'min_reputation': int,
    'required_aura_vision': int,
    'totem_category': int,
    'totem_category1': int,
    'required_area_group_id': int,
    'school_mask': int,
    'rune_cost_id': int,
    'spell_missile_id': int,
    'power_display_id': int,
    'effect_bonus_multiplier': float,
    'effect_bonus_multiplier1': float,
    'effect_bonus_multiplier2': float,
    'spell_description_variable_id': int,
    'spell_difficulty_id': int
}

SpellRecord = dataclasses.make_dataclass('SpellRecord', zip(_fields.keys(), _fields.values()))
SpellRecord.field_types = staticmethod(_fields.values())

